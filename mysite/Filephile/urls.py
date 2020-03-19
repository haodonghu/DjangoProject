from django.urls import path

from . import views

app_name = 'Filephile'
urlpatterns = [
    path('', views.index, name='index'), # or 'index/'
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload/', views.upload, name='upload'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('download/<path:file_path>', views.download, name='download'),
    path('creategroup/', views.create_group, name='create_group'),
    path('groups/<int:id>/', views.groups, name='groups'),
    path('addorquit/<int:id>/', views.add_or_quit, name='add_or_quit'),
    path('groupinfo/<int:id>/', views.group_info, name='group_info'),
    path('searchgroup/', views.search_group, name='search_group'),
    path('join/<int:id>/', views.join, name='join'),
    path('quit/<int:id>/', views.quit, name='quit'),
    path('dismiss/<int:id>/', views.dismiss, name='dismiss'),
    path('changename/', views.change_name, name='change_name'),
    path('changepassword/', views.change_password, name='change_password'),
    path('setting/<int:id>/', views.setting, name='setting'),
]
