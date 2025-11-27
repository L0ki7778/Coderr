from django.db import models
from accounts.models import User
from .offers import Details


class Orders(models.Model):
    IN_PROGRESS:"in_progress"
    COMPLETED:"completed"

    ORDER_STATES={
        IN_PROGRESS : "in_progress",
        COMPLETED : "completed"
    }

    customer_user= models.ForeignKey(User, on_delete=models.CASCADE)
    business_user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=ORDER_STATES, default=IN_PROGRESS)
