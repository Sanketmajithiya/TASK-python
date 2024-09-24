from django.db import models

# Create your models here.
class student(models.Model):
    profile = models.ImageField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    City = models.CharField(max_length=255)
    
    
