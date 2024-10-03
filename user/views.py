from .serializers import *
from .models import *
from rest_framework import viewsets,status
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import login,authenticate
from django.views.decorators.csrf import csrf_exempt
import logging
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
class UserRegistrationView(APIView):
   def post(self,request):
       serializer = UserSerializer(data=request.data)
       if serializer.is_valid():
           user = serializer.save()  # Save the user instance
           user_data = UserSerializer(user).data

           return Response(user_data, status=status.HTTP_201_CREATED)

       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

logger = logging.getLogger(__name__)


class CustomTokenObtainPairView(TokenObtainPairView):
    pass
class UserRoleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        user_role = request.user.role
        return Response({'role': user_role})


class JobListingViewSet(viewsets.ModelViewSet):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer


    def get_queryset(self):
        user = self.request.user

        if user.role == 'Employer':
            return JobListing.objects.filter(company__owner=user)
        elif user.role == 'Admin':
            return JobListing.objects.all()
        else:  # Candidate role
            return JobListing.objects.filter(is_active=True)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()

class CreateCompany(APIView):
    def post(self,request):
        user = self.request.user
        if user.role == 'Employer' or user.role == 'Admin':
            serializer = CompanySerializer(data=request.data)
            if serializer.is_valid():
                company = serializer.save()
                company_data = CompanySerializer(company).data
                return Response(company_data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Cannot Create",status=status.HTTP_401_UNAUTHORIZED)

class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

    def get_queryset(self):
        user = self.request.user

        if user.role == 'Candidate':
            return JobApplication.objects.filter(candidate=user)
        elif user.role == 'Employer':
            return JobApplication.objects.filter(job__company__owner=user)
        elif user.role == 'Admin':
            return JobApplication.objects.all()
        return JobApplication.objects.none()

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()


class LogoutView(APIView):
    def post(self, request):
        try:
            # Get the refresh token from the request
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)

            # Blacklist the refresh token
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

