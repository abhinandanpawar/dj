from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def dj(request):
    a=[1,2,3,4]
    return HttpResponse(i for i in a )
