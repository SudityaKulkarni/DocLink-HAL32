from django.db import models
from doctors.models import Doctor
from patients.models import User

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key to User
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)  # Foreign key to Doctor
    slot_date = models.CharField(max_length=255)
    slot_time = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    cancelled = models.BooleanField(default=False)
    payment = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

    # def _str_(self):
    #     return f"Appointment {self.id} - User: {self.user.username}, Doctor: {self.doctor.name}"
