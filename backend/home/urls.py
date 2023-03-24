from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('user/', views.user,name='user'),
    path('task/', views.task,name='task'),
]