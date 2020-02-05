from django.urls import path

from . import views

app_name = 'Filephile'
urlpatterns = [
    path('', views.index, name='index'), # or 'index/'
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]
