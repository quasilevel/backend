from django.shortcuts import render
from rest_framework import viewsets
from .serializers import fractalserializer
from fractal.models import task
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class task(viewsets.ModelViewSet):
    queryset = task.objects.all()
    serializer_class = fractalserializer
    #authentication_classes = [SessionAuthentication]
    #permission_classes = [IsAuthenticatedOrReadOnly]

