from rest_framework import generics
from .models import Patient
from .serializers import PatientSerializer

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
 
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PateintRegisterView(generics.CreateAPIView):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

 