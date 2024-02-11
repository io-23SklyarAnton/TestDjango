from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.hello, name='my-view'),
    path("showform/", views.showform, name="showform"),
    path("getform/", views.getform, name="getform"),
]
