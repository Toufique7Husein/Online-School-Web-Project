from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [
    path('materials', views.materials, name = 'materials'),
    path('readPdf/<id>/', views.readPdf, name = 'readPdf'),
]