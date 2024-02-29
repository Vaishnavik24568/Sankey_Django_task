from django.db import models
from django.core.validators import RegexValidator


class Booking(models.Model):
    ticket_id = models.CharField(
        primary_key=True,
        max_length=10,
        validators=[RegexValidator(regex=r'^TK\d{8}$', message='Invalid ticket id')]
    )
    trip_id = models.CharField(
        max_length=10,
        validators=[RegexValidator(regex=r'^TP\d{8}$', message='Invalid Trip id')]
    )
    traveler_name = models.CharField(max_length=255)
    traveler_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(regex=r'^\d{10,15}$', message='Invalid phone number')]
    )
    ticket_cost = models.DecimalField(max_digits=10, decimal_places=2)
    traveler_email = models.EmailField(
        validators=[RegexValidator(regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', message='Invalid email')]
    )