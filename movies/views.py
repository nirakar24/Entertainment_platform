from datetime import datetime, timedelta
from django.shortcuts import render
from .models import Movie

def latest_releases(request):
    latest_releases = Movie.objects.filter(release_date__gte=datetime.now() - timedelta(days=40))
    
    return render(request, 'latest_releases.html', {'latest_releases': latest_releases})
