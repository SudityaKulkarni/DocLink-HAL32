from rest_framework import generics  ,status
from .models import Patient
from .serializers import PatientSerializer

class PatientListView(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
 
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientRegisterView(generics.CreateAPIView):

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        patient_id = request.data.get('patient_id')  # Assuming you send the patient's ID with the image
        try:
            patient = Patient.objects.get(id=patient_id)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)

        # Save the image
        patient.image = request.data.get('image')
        patient.save()

        return Response({"message": "Image uploaded successfully"}, status=status.HTTP_200_OK)