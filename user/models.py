# custom_auth/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.hashers import make_password

class User(AbstractUser):
    ROLE_CHOICES = [
        ('Candidate', 'Candidate'),
        ('Employer', 'Employer'),
        ('Admin', 'Admin'),
    ]
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Candidate')

    def __str___(self):
        return self.role
class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE, limit_choices_to={'role': 'Employer'})

class JobListing(models.Model):
    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]
    job = models.ForeignKey(JobListing,on_delete=models.CASCADE)
    candidate = models.ForeignKey(User,on_delete=models.CASCADE,limit_choices_to={'role': 'Candidate'})
    resume = models.FileField(upload_to='resume/')
    cover_letter = models.TextField(blank=True,null=True)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='Pending')