#Sergio González Muriel
from django.urls import path

from . import views

urlpatterns = [
    path('welcome', views.welcome, name='welcome'),
    path('health-check', views.health_check, name='health-check'),
    path('login', views.login, name='login'),
    path('check-login', views.check_login, name='check-login'),
]