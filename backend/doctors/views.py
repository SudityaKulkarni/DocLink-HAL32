from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer, DoctorRegisterSerializer

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
 
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorRegisterView(generics.CreateAPIView):

    queryset = Doctor.objects.all()
    serializer_class = DoctorRegisterSerializer

 