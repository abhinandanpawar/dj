from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fees(request):
    return HttpResponse("hello fees is 100000")

