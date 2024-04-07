from django.urls import path
from .views import latest_releases

urlpatterns = [
    path('latest/', latest_releases, name='latest_releases'),
]
