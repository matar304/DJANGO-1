from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'registration/login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def user_profile(request):
    return render(request, 'profile.html')

def logout_view(request):
    logout(request)
    return redirect('login')