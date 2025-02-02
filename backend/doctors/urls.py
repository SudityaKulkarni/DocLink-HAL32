from django.urls import path
from rest_framework import permissions
from .views import DoctorDetailView, DoctorRegisterView

from .views import ImageUploadView


urlpatterns = [
    path('<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('register-doctor/', DoctorRegisterView.as_view(), name='doctor-register'),

    path('upload/', ImageUploadView.as_view(), name="image-upload"),
]

