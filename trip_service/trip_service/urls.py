# Trip_services/urls.py
from django.urls import path, include

urlpatterns = [
    path('trip/', include('Trip.urls')),
    path('route/', include('Route.urls')),
]
