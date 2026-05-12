from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    #api endpoints
    return HttpResponse("Welcome to the Students Home Page")