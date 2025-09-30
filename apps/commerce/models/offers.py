from django.db import models

from apps.accounts.models import User


class Offers(models.Model):
    creator_id = models.ForeignKey(User, unique=True, null=False, blank=False)
    min_price = models.FloatField(default=1.00)
    max_delivery_time = models.IntegerField()
