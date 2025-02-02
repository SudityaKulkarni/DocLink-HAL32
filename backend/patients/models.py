from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    image = models.ImageField(upload_to='patient_images/',blank = True ,null = True)
    address_line1 = models.CharField(max_length=255, blank=True, default="")
    address_line2 = models.CharField(max_length=255, blank=True, default="")
    gender = models.CharField(max_length=50, default="Not Selected")
    dob = models.DateField()
    phone = models.CharField(max_length=10, default="0000000000")
