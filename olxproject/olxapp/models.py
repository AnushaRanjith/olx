from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.




class OlxModel(AbstractUser):
    cus_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.CharField(max_length=100)
    
