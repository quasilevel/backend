from django.contrib import admin
from django.urls import path,include
from fractal import views

urlpatterns = [
    path('fractal/', views.show),
    path('task/', views.get, name='task-list'),
    path('task/<int:pk>/', views.post,name='task-create'),
    path('api-auth/',include('rest_framework.urls')),
     
]