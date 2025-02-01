from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)  # Manually defining the `id` field
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    experience = models.TextField(blank=True, default="")
    about = models.TextField(blank=True, default="")
    available = models.BooleanField(default=True)
    fees = models.PositiveIntegerField()
    address = models.JSONField()
    join_date = models.DateField(default=timezone.now)
    slots_booked = models.JSONField(null=True)


    def __str__(self):
        return self.email








