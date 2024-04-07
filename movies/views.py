from datetime import datetime, timedelta
from django.shortcuts import render
from .models import Movie

def latest_releases(request):
    # Fetch latest releases (movies released within the last month)
    latest_releases = Movie.objects.filter(release_date__gte=datetime.now() - timedelta(days=30))
    
    return render(request, 'movies/latest_releases.html', {'latest_releases': latest_releases})
