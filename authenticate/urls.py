from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password', views.change_password, name='change_password'),
    path('showuser/', views.showuser, name='showuser'),
    path('adduser', views.adminadduser, name='adduser'),
    path('edit_user/(?p<id>\d+/$)', views.adminedituser, name='edit_user'),
    path('del_user/(?p<id>\d+/$)',views.del_user,name='del_user'),
]
