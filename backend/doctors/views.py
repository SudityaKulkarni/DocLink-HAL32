from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from .models import Doctor
from .serializers import DoctorSerializer, DoctorRegisterSerializer, GetAllDoctorsSerializer

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorRegisterView(generics.CreateAPIView):

    queryset = Doctor.objects.all()
    serializer_class = DoctorRegisterSerializer

@api_view(['GET'])
def get_all_doctors(request):
    doctors = Doctor.objects.all()
    serializer = GetAllDoctorsSerializer(doctors, many=True)
    data = {
        "success": "true",
        "doctors": serializer.data
    }
    return Response(data)

@api_view(['POST'])
def change_availibity(request):
    doc_id = request.data.get('docId')
    try:
        doctor = Doctor.objects.get(id=doc_id)  # Find doctor
        doctor.available = not doctor.available
        doctor.save()  # Save changes
    
    except Doctor.DoesNotExist:
        return Response({
            "sucess": "false",
            "error": "Doctor not found"
            }, status=status.HTTP_404_NOT_FOUND)

    return Response({
        "success": "true",
        "message": "availibility updated successfully"
    })
