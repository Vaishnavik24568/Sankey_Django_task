from django.urls import path, include

urlpatterns = [
    path('booking/', include('Booking.urls')),
]
