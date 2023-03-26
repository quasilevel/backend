from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse("THIS IS HOMEPAGE...")

def member(request):
    return HttpResponse("USER...")