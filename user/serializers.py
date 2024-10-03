from rest_framework import serializers
from .models import User,Company,JobListing,JobApplication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'role']

    def create(self, validated_data):
        # Hash the password here before saving the user
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','name','location','description','owner']

class JobListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobListing
        fields = ['id', 'title', 'company', 'description', 'requirements', 'location', 'salary', 'created_at','is_active']

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = ['id', 'job', 'candidate', 'resume', 'cover_letter', 'applied_at', 'status']