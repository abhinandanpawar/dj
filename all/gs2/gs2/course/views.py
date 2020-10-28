from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def django(request):
    return HttpResponse("Learn Django")
def python(request):
    return HttpResponse("Learn python")
def djangoPython(request):
    return HttpResponse("Learn Django and python")
def pythonDjango(request):
    return HttpResponse("Learn django and python")
