from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    username=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    message=models.TextField()

# Create your models here.

