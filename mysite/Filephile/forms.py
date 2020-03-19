from django import forms
from captcha.fields import CaptchaField

class UserForm(forms.Form):
    username = forms.CharField(label="username", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label="verification-code")


class RegisterForm(forms.Form):
    username = forms.CharField(label="username", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="confirm-password", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='verification-code')


class UploadFileForm(forms.Form):
    filename = forms.CharField(label="filename", max_length=50)
    filedata = forms.FileField(label="filedata")


class CreateGroupForm(forms.Form):
    groupname = forms.CharField(label="groupname", max_length=50)
    permission_key = forms.CharField(label="permission_key", max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class SearchGroupForm(forms.Form):
    groupname = forms.CharField(label="groupname", max_length=50)


class JoinGroupForm(forms.Form):
    permission_key = forms.CharField(label="permission_key", max_length=50, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ChangeNameForm(forms.Form):
    change = forms.CharField(label="change", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))


class ChangePasswordForm(forms.Form):
    current = forms.CharField(label="current", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    change = forms.CharField(label="change", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
