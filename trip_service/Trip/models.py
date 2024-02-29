from django.db import models
from Route.models import Route
class Trip(models.Model):
    trip_id = models.CharField(max_length=10, primary_key=True)
    user_id = models.IntegerField()
    vehicle_id = models.IntegerField()
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE) 
    driver_name = models.CharField(max_length=100)
    trip_distance = models.FloatField()
