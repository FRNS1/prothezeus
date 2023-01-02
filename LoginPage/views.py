from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .urls import *

# Create your views here.


def LoginPage(request):
    if request.method == 'POST':

        username = request.POST['login']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage/')
        else:
            return redirect('/')
    else:
        return render(request, 'Pages/loginpage.html')


def homepage(request):
    return render(request, 'Pages/homepage.html')
