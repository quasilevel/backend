from django.contrib import admin
from django.urls import path,include
from fractal import views
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('task', taskviewset)

urlpatterns = [
    path('',include(router.urls)),
    path('task/', views.get, name='task-list'),
    path('task/<int:pk>/', views.post,name='task-create'),
     
]
