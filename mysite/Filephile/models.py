from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=40, null=True,default="null")
    permission_key = models.CharField(max_length=256, blank=True, null=True)
    Date_Created = models.DateTimeField(auto_now_add=True)


class User(models.Model):
    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    c_time = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(Group, blank=True)


class File(models.Model):
    name = models.CharField(max_length=40)
    data = models.FileField(upload_to='Filephile/static/files')
    Date_Added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    private = models.BooleanField(default=True)
    groups = models.ManyToManyField(Group, blank=True)


class Manager(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)
