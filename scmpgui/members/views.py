from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
import time

from .templates.forms import CreatUserForm

from django.contrib.auth.decorators import login_required

# Create your views here.
def register_page(request):

    if request.user.is_authenticated:
        return redirect('home')
    
    else:

        form = CreatUserForm()

        if request.method == 'POST':
            form = CreatUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Account Created Successfully!', extra_tags='success')
                return redirect('members_login')
            else:
                messages.info(request, 'There was an error signing up!', extra_tags='error')

        context = {'form':form}
        return render(request, 'members/register.html', context)

def login_page(request):

    if request.user.is_authenticated:
        return redirect('home')
    
    else:
    
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
    return redirect('members_login')


