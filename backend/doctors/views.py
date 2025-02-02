from rest_framework import generics  ,status
from .models import Doctor
from .serializers import DoctorSerializer, DoctorRegisterSerializer

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
 
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorRegisterView(generics.CreateAPIView):

    queryset = Doctor.objects.all()
    serializer_class = DoctorRegisterSerializer

 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        doctor_id = request.data.get('doctor_id')  # Assuming you send the doctor's ID with the image
        try:
            doctor = Doctor.objects.get(id=doctor_id)
        except Doctor.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)

        # Save the image
        doctor.image = request.data.get('image')
        doctor.save()

        return Response({"message": "Image uploaded successfully"}, status=status.HTTP_200_OK)