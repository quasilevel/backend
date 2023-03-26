from django.contrib import admin
from django.urls import path
from member import views

urlpatterns = [
    path('', views.index, name='home'),
    path('member/', views.member,name='user'),
]