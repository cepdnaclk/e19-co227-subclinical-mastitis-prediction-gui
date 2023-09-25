from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse

from .templates.forms import CreatUserForm

# Create your views here.

def register_page(request):
    form = CreatUserForm()

    if request.method == 'POST':
        form = CreatUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully!')
            return redirect('login')
        else:
            messages.info(request, 'There was an error signing in!')

    context = {'form':form}
    return render(request, 'authenticate/register.html', context)

def login_page(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('home'))
        else:
            messages.info(request, 'There was an error loggin in!')

    context = {}
    return render(request, 'authenticate/login.html', context)

