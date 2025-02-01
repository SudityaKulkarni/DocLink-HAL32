from django.urls import path
from rest_framework import permissions
from .views import DoctorDetailView, DoctorRegisterView



urlpatterns = [
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('doctors/register-doctor/', DoctorRegisterView.as_view(), name='doctor-register'),
]

