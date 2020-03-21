from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from .forms import UserForm, RegisterForm, UploadFileForm, CreateGroupForm, SearchGroupForm, JoinGroupForm, ChangeNameForm, ChangePasswordForm
from . import models
import hashlib, os

def hash_code(s, salt='mysite'): # add a hash function to encode the password
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()

# Create your views here.
def index(request):
    pass
    return render(request, 'Filephile/index.html')

def change_name(request):
    if not request.session.get('is_login',None):
        return redirect('/')
    if request.method == "GET":
        change_name_form = ChangeNameForm()
        return render(request, "Filephile/change_name.html", locals())
    elif request.method == "POST":
        change_name_form = ChangeNameForm(request.POST)
        if change_name_form.is_valid():
            user = models.User.objects.get(name=request.session['user_name'])
            user.name = change_name_form.cleaned_data['change']
            request.session['user_name'] = user.name
            user.save()
            return redirect('/')
    return redirect('/')

def change_password(request):
    if not request.session.get('is_login',None):
        return redirect('/')
    if request.method == "GET":
        change_password_form = ChangePasswordForm()
        return render(request, "Filephile/change_password.html", locals())
    elif request.method == "POST":
        change_password_form = ChangePasswordForm(request.POST)
        if change_password_form.is_valid():
            user = models.User.objects.get(name=request.session['user_name'])
            current_password = change_password_form.cleaned_data['current']
            if user.password == hash_code(current_password):
                change = change_password_form.cleaned_data['change']
                user.password = hash_code(change)
                user.save()
                return redirect('/')
            return HttpResponse('current password does not match')
    return redirect('/')

def setting(request, id):
    if not request.session.get('is_login',None):
        return redirect('/')

    targeted_user = models.User.objects.get(id=id)

    user = models.User.objects.get(name=request.session['user_name'])

    return render(request, "Filephile/setting.html", locals())


def join(request, id):
    if not request.session.get('is_login',None):
        return redirect('/')

    if request.method == "GET":
        return redirect('/dashboard/')
    elif request.method == "POST":
        join_group_form = JoinGroupForm(request.POST)
        if join_group_form.is_valid():
            permission_key = join_group_form.cleaned_data['permission_key']
            group = models.Group.objects.get(id=id)
            if permission_key == group.permission_key:
                user = models.User.objects.get(name=request.session['user_name'])
                group.user_set.add(user)
                return redirect('/dashboard/')
    return redirect('/dashboard/')

def quit(request, id):
    if not request.session.get('is_login',None):
        return redirect('/')

    group = models.Group.objects.get(id=id)

    user = models.User.objects.get(name=request.session['user_name'])

    group.user_set.remove(user)

    return redirect('/dashboard/')

def dismiss(request, id):
    if not request.session.get('is_login',None):
        return redirect('/')

    group = models.Group.objects.get(id=id)

    group.delete()

    return redirect('/dashboard/')

def search_group(request):
    if not request.session.get('is_login',None):
        return redirect('/')
    if request.method == "GET":
        return redirect('/dashboard/')
    elif request.method == "POST":
        search_group_form = SearchGroupForm(request.POST)
        if search_group_form.is_valid():
            search_group_name = search_group_form.cleaned_data['groupname']
            results = models.Group.objects.filter(name=search_group_name)
            if results:
                user = models.User.objects.get(name=request.session['user_name'])
                group = models.Group.objects.get(name=search_group_name)
                user_number = group.user_set.all().count()
                users = group.user_set.all()
                manager = models.Manager.objects.get(group=group.id)
                join_group_form = JoinGroupForm()
                return render(request, "Filephile/group_info.html", locals())
            else:
                return HttpResponse("No result")
        return redirect('/dashboard/')
    return redirect('/dashboard/')


def group_info(request, id):
    if not request.session.get('is_login',None):
        return redirect('/')

    user = models.User.objects.get(name=request.session['user_name'])

    group = models.Group.objects.get(id=id)

    user_number = group.user_set.all().count()

    file_number = group.file_set.all().count()

    users = group.user_set.all()

    files = group.file_set.all()

    manager = models.Manager.objects.get(group=id)

    return render(request, "Filephile/group_info.html", locals())

def add_or_quit(request, id):
    if request.method == "GET":
        return redirect('/dashboard/')
    elif request.method == "POST":
        group_ids = request.POST.getlist('group',[])
        file = models.File.objects.get(id=id)
        file.groups.clear()
        groups = []
        for group_id in group_ids:
            group = models.Group.objects.get(id=group_id)
            file.groups.add(group)
        if file.groups.count() == 0:
            file.private = True
        else:
            file.private = False
        file.save()
        return redirect('/dashboard/')

def groups(request, id):
    if not request.session.get('is_login',None):
        return redirect('/')

    user = models.User.objects.get(name=request.session['user_name'])

    groups_all = user.groups.all()

    file = models.File.objects.get(id=id)

    groups_in = file.groups.all()

    return render(request, 'Filephile/group_list.html', locals())

def create_group(request):
    if not request.session.get('is_login',None):
        return redirect('/')

    if request.method == "GET":
        return redirect('/dashboard/')
    elif request.method == "POST":
        create_group_form = CreateGroupForm(request.POST)
        if create_group_form.is_valid():
            group_name = create_group_form.cleaned_data['groupname']
            permission_key = create_group_form.cleaned_data['permission_key']
            new_group = models.Group.objects.create()
            new_group.name = group_name
            new_group.permission_key = permission_key
            new_group.save()
            # add creater
            group = models.Group.objects.get(name=group_name)
            current_user = models.User.objects.get(name=request.session['user_name'])
            current_user.groups.add(group)
            new_manager = models.Manager.objects.create()
            new_manager.name = current_user
            new_manager.group = group
            new_manager.save()
            return redirect('/dashboard/')
        return render(request, 'Filephile/dashboard.html', {"message":message})
    return redirect('/dashboard/')


def download(request, file_path):
    response = FileResponse(open(file_path, 'rb'))
    response['content_type'] = "application/octet-stream"
    response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
    return response

def delete(request, id):
    if not request.session.get('is_login',None):
        return redirect('/')

    file = models.File.objects.get(id=id)
    file.delete()
    return redirect('/dashboard/')

def upload(request):
    if not request.session.get('is_login',None):
        return redirect('/')

    if request.method == "GET":
        return redirect('/dashboard/')
    elif request.method == "POST":
        upload_form = UploadFileForm(request.POST, request.FILES)
        if upload_form.is_valid():
            filename = upload_form.cleaned_data['filename']
            filedata = upload_form.cleaned_data['filedata']
            fileowner = models.User.objects.get(name=request.session['user_name'])
            file = models.File.objects.create()
            file.name = filename
            file.data = filedata
            file.owner = fileowner
            file.save()
            return redirect('/dashboard/')
    return redirect('/dashboard/')

def dashboard(request):
    if not request.session.get('is_login',None):
        return redirect('/')

    user = models.User.objects.get(name=request.session['user_name'])

    groups = user.groups.all()

    files = user.file_set.all()

    # access the "File table" in database
    # make a table to show files whose owner is the current user
    upload_form = UploadFileForm()
    create_group_form = CreateGroupForm()
    search_group_form = SearchGroupForm()
    return render(request, "Filephile/dashboard.html", locals())

def login(request):
    # Dupicate logins are not allowed
    if request.session.get('is_login',None):
        return redirect('/')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "Please check again"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = models.User.objects.get(name=username)
                if user.password == hash_code(password):
                    # write user status and data
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/') # or '/index/'
                else:
                    message = "wrong password or username"
            except:
                message = "wrong password or username"
        return render(request, 'Filephile/login.html', locals())

    login_form = UserForm()
    return render(request, 'Filephile/login.html', locals())

def register(request):
    if request.session.get('is_login', None):
        # you cannot register if you are logged in
        return redirect("/")

    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "Please use real information"
        if register_form.is_valid():  # get data
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            if password1 != password2:  # check confirm password
                message = "the two passwords you entered are different"
                return render(request, 'Filephile/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # check if the username is already existed
                    message = 'username exsited'
                    return render(request, 'Filephile/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # check if the email is already existed
                    message = 'email existed'
                    return render(request, 'Filephile/register.html', locals())

                # when everything is ok, create a new user
                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = hash_code(password1)
                new_user.email = email
                new_user.save()
                user = models.User.objects.get(name=username)
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                return redirect('/')  #jump to index page
    register_form = RegisterForm()
    return render(request, 'Filephile/register.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        # if you did not log in, you could not log out
        return redirect("/")
    request.session.flush() # del everything
    # or use the method below
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/")
