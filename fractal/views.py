from django.shortcuts import render,HttpResponse
from .models import task
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from .serializers import taskserializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import viewsets

@csrf_exempt 
def get(request):
    fractal = task.objects.all()
    serializer = taskserializer(fractal, many=True)
    return HttpResponse(serializer.data)

@csrf_exempt
def post(request):
          serializer = taskserializer(data=request.data)
          if serializer.is_valid():            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
          else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class taskviewset(viewsets.ModelViewSet):
     queryset = task.objects.all()
     serializer_class = taskserializer