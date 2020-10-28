from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def learn_django(request):
    a=[1,2,3,4,5]
    return HttpResponse(print(i) for i in a)