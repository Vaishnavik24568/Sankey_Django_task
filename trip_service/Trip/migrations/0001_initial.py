# Generated by Django 5.0.2 on 2024-02-27 17:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Route", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Trip",
            fields=[
                (
                    "trip_id",
                    models.CharField(max_length=12, primary_key=True, serialize=False),
                ),
                ("user_id", models.IntegerField()),
                ("vehicle_id", models.IntegerField()),
                ("driver_name", models.CharField(max_length=255)),
                ("trip_distance", models.FloatField()),
                (
                    "route",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Route.route"
                    ),
                ),
            ],
        ),
    ]