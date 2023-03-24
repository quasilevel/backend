from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse("this is homepage")

def user(request):
    return HttpResponse("user")

def task(request):
    return HttpResponse("task")