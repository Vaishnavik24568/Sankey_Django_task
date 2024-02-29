from django.db import models

class Route(models.Model):
    route_id = models.CharField(max_length=10, primary_key=True)
    user_id = models.IntegerField()
    route_name = models.CharField(max_length=100)
    route_origin = models.CharField(max_length=100)
    route_destination = models.CharField(max_length=100)
    stops = models.JSONField()

def __str__(self):
    return self.route_name