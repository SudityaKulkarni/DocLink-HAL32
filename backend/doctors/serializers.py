from rest_framework import serializers
from .models import Doctor

class DoctorRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            'id', 
            'username',
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

class GetAllDoctorsSerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()

    
    _id = serializers.SerializerMethodField()

    class Meta:
        model = Doctor
        fields = [
            '_id', 
            'name',
            'speciality',
            'degree',
            'experience',
            'about',
            'available',
            'fees', 
            'address',
            'join_date',
            'slots_booked'
        ]
    
    
    def get_name(self, obj):
        return obj.username
    
    def get__id(self, obj):
        return obj.id
 