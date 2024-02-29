from django.contrib import admin
from django.urls import path
from Trip import views

urlpatterns = [
    path("/create", views.create_trip, name='create_trip'),
    path('/trips/', views.TripListAPIView.as_view(), name='trip-list'),
    path("/trips/<str:trip_id>/", views.TripDetailAPIView.as_view(), name='trip-detail'),

]
