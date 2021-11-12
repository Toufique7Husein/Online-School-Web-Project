from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('classroom', views.classroom, name = 'classroom'),
    path('creatclass', views.creatclass, name='creatclass'),
    path('joinclass', views.joinclass, name='joinclass'),
    path('enterClass/<id>/', views.enterClass, name='enterClass'),
    path('people', views.people, name = 'people'),
    path('upload_material', views.upload_material, name = 'upload_material'),
]