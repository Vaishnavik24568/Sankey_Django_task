# Generated by Django 5.0.2 on 2024-02-27 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Trip", "0002_alter_trip_driver_name_alter_trip_trip_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="trip",
            old_name="route",
            new_name="route_id",
        ),
    ]
