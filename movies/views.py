from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from .models import Trailer, Movie

def home(request):
    trending_trailers = Trailer.objects.all()[:5]  
    latest_releases = Movie.objects.order_by('-release_date')[:10] 
    return render(request, 'home.html', {'trending_trailers': trending_trailers, 'latest_releases': latest_releases})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Replace 'home' with the name of your home page URL
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')  # Replace 'home' with the name of your home page URL

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Replace 'login' with the name of your login page URL
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
