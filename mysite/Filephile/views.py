from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm, RegisterForm
from . import models
import hashlib

def hash_code(s, salt='mysite'): # add a hash function to encode the password
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()

# Create your views here.
def index(request):
    pass
    return render(request, 'Filephile/index.html')

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
