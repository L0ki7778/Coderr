from django.db import models
from django.contrib.auth.models import AbstractUser

    
class User(AbstractUser):
    ROLE_CHOICES = [
        ("customer", "Customer"),
        ("offerer", "Offerer")
    ]

    type = models.CharField(choices=ROLE_CHOICES,  max_length=20)
    file = models.ImageField(upload_to="profiles/", blank=True, null=True)
    location = models.CharField(max_length=120, blank=True)
    tel = models.CharField(max_length=20, blank=True)
    description = models.TextField( blank=True)
    working_hours = models.CharField( blank=True)
    created_at = models.DateTimeField(auto_now_add=True)