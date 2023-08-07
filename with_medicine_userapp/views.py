from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('main')
        else:
            return redirect('signup')
    else:
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form' : form})
    
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('main')
        else:
            return redirect('login')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form' : form})
    
def logout(request):
    auth.logout(request)
    return redirect('main')