from django.contrib import admin
from django.urls import path
from Booking import views

urlpatterns = [
    path("", views.index , name='home'),
    path("create", views.create , name='create'),
    path('bookings/', views.BookingListAPIView.as_view(), name='booking-list'),
    path('booking/<str:ticket_id>/', views.BookingDetailAPIView.as_view(), name='booking-detail'),

]
