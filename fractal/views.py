from django.shortcuts import render,HttpResponse
from .models import task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.serializers import fractalserializer
 
@api_view(['GET'])
def get(request):
    fractal = task.objects.all()
    serializer = fractalserializer(fractal, many=True)
    return HttpResponse(serializer.data)

@api_view(['POST'])  
def post(request):
          serializer = fractalserializer(data=request.data)
          if serializer.is_valid():            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
          else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def show(request):
      return HttpResponse("task...")