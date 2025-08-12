from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USER_TYPES =[
        ('customer', 'customer'),
        ('offerer', 'offerer')
    ]
    
    type = models.CharField(max_length=10, choices=USER_TYPES, default='customer')