from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def learn(request):
    return HttpResponse("hello learn django")

