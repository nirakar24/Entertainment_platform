from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from datetime import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .models import Trailer, Movie, UserProfile

@login_required
def add_to_wishlist(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    user_profile.wishlist.add(movie)
    messages.success(request, f'{movie.title} has been added to your wishlist.', extra_tags='alert')
    return redirect('movie_details', movie_id=movie_id)

@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    wishlist = user_profile.wishlist.all()
    return render(request, 'profile.html', {'wishlist': wishlist})

def movie_details(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    trailers = [movie.trailer] if movie.trailer else []  
    return render(request, 'movie_details.html', {'movie': movie, 'trailers': trailers})

def home(request):
    latest_releases = Movie.objects.order_by('-release_date')[:5]
    today = datetime.now().date()
    last_month = today - timedelta(days=30)
    spotlight_movies = Movie.objects.filter(release_date__gte=last_month) 
    return render(request, 'home.html', {'latest_releases': latest_releases, 'spotlight_movies': spotlight_movies})

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
