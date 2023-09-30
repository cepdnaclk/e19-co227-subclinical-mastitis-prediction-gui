from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
import time

from .templates.forms import CreatUserForm

# Create your views here.

def initial_page(request):
    return render(request, 'members/initial.html')
    
def front_page(request):
    return render(request, 'members/front.html')

def register_page(request):
    form = CreatUserForm()

    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully!', extra_tags='success')
            return redirect('login')
        else:
            messages.info(request, 'There was an error signing up!', extra_tags='error')

    context = {'form':form}
    return render(request, 'members/register.html', context)

def login_page(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('home'))
        else:
            messages.info(request, 'There was an error loging in!', extra_tags='error')

    context = {}
    return render(request, 'members/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('front')


