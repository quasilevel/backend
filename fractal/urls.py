from django.contrib import admin
from django.urls import path
from fractal import views

urlpatterns = [
    path('fractal/', views.fractal,name='task'),
]