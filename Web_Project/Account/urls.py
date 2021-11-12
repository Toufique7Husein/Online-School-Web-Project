from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('',views.login, name = 'login'),
    path('signup', views.signup, name = 'signup'),
    path('logout', views.logout, name = 'logout')
]
