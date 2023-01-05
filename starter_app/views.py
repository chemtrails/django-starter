from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
# Create your views here.

def index(request):
    return render(
        request,
        'index.html'
    )

def login(request):
    err = False
    
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            return redirect('index')
        else:
            err = True

    return render(
        request,
        'registration/login.html',
        {
            'error': err
        }
    )

def logout(request):
    return redirect('index')

def register(request):
    err = False

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            err = True

    return render(
        request,
        'registration/register.html',
        {
            'error': err
        }
    )
    