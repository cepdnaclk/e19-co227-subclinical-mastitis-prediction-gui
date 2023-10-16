from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

# Create your views here.

@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def HomePageView(request):
    return render(request, 'home/homepage.html')