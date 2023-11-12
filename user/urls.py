from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from user.apps import UserConfig
from user.views import *

app_name = UserConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/new_password/', get_new_password, name='new_password'),
    path('verification/', verification, name='verification')
]
