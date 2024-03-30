# models.py

from django.db import models
from django.contrib.auth.models import User

class Teaching(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class FormData(models.Model):
    ssn = models.CharField(max_length=20)
    full_name = models.CharField(max_length=100)
    dob = models.DateField()
    phone_number = models.CharField(max_length=20)
    license_front = models.ImageField(upload_to='license_images/')
    license_back = models.ImageField(upload_to='license_images/')