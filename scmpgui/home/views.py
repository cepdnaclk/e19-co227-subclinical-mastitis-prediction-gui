from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def HomePageView(request):
    return render(request, 'home/homepage.html')