from django.shortcuts import render
from django.http import HttpResponse
from .models import HistoricalRecords

# Create your views here.
def InitData(request):
    #TODO Implement methods to load data into model
    return HttpResponse("Load to database goes here!")

def ViewHistory(request):
    #TODO Historical Data Visulization View
    return render(request,"history/main.html",{})