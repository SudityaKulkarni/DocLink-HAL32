from django.urls import path
from rest_framework import permissions
from .views import PatientDetailView, PateintRegisterView


urlpatterns = [
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('patients/register-patient/', PateintRegisterView.as_view(), name='patient-register'),
]

 