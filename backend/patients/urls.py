from django.urls import path
from rest_framework import permissions
from .views import PatientDetailView, PatientRegisterView ,PatientListView

from .views import ImageUploadView

urlpatterns = [
    path('', PatientListView.as_view(), name='patient-list'),
    path('<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('register-patient/', PatientRegisterView.as_view(), name='patient-register'),

    path("upload/", ImageUploadView.as_view(), name="image-upload"),

]

