from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import auth


def index(request):
    return render(
        request,
        'index.html'
    )

def login(request):
    form = None
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return redirect('index')
    
    return render(
        request,
        'registration/login.html',
        {
            'form': form
        }
    )

def logout(request):
    auth.logout(request)
    return redirect('index')

def register(request):
    form = None

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(
        request,
        'registration/register.html',
        {
            'form': form
        }
    )
    