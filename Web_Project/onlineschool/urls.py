from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('home', views.home, name = 'home'),
    path('profile', views.profile, name = 'profile'),
    path('edit_profile', views.edit_profile, name = 'edit_profile'),
]
