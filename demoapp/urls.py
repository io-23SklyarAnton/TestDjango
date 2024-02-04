from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.hello, name='my-view'),
    path('second/', views.second_page, name='second page')
]
