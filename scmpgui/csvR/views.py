from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def csvR(request):
    return render(request,'csvR.html')