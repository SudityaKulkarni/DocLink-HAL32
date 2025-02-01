from rest_framework import serializers
from .models import Doctor

class DoctorRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            'id', 
            'name',
            'email',
            'password',
            'speciality',
            'degree',
            'experience',
            'about',
            'fees',
            'address',
            'join_date'
        ]
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'