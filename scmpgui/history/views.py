from django.shortcuts import render
from django.http import HttpResponse
from .models import HistoricalRecords
from .files import InitHistory

# Create your views here.
def InitData(request):
    InitHistory()
    return HttpResponse("Databse Loaded!")

def ViewHistory(request):
    #TODO Historical Data Visulization View
    return render(request,"history/main.html",{})