from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    image = models.ImageField(upload_to='doctor_images/',blank = True ,null = True)
    speciality = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    experience = models.TextField(blank=True, default="")
    about = models.TextField(blank=True, default="")
    available = models.BooleanField(default=True)
    fees = models.PositiveIntegerField()
    address = models.JSONField()
    join_date = models.DateField()
    slots_booked = models.JSONField(null=True)




