from django.db import models
from apps.accounts.models import User
from .offers import Details


class Orders(models.Model):
    IN_PROGRESS="in_progress"
    COMPLETED="completed"
    CANCELLED="cancelled"

    ORDER_STATES={
        IN_PROGRESS : "in_progress",
        COMPLETED : "completed",
        CANCELLED:"cancelled"
    }

    customer_user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="customer")
    business_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="offerer")
    status = models.CharField(max_length=20, choices=ORDER_STATES, default=IN_PROGRESS)
    offer_detail = models.ForeignKey(Details, on_delete=models.PROTECT,related_name="details")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
