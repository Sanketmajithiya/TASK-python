from django.db import models

# Create your models here.

class Student(models.Model):
    
    Name = models.CharField(max_length=50)
    Image = models.ImageField(upload_to="img/")
    Email = models.EmailField(max_length=255)
    City = models.CharField(max_length=255)
    Number = models.BigIntegerField()
   