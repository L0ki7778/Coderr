from django.db import models

from apps.accounts.models import User


class Offers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=30, blank=False, null=False)
    image = models.ImageField(null=True)
    description = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Details(models.Model):
    BASIC = "basic"
    STANDARD = "standard"
    PREMIUM = "premium"

    OFFER_TYPES = {
        BASIC: "basic",
        STANDARD: "standard",
        PREMIUM: "premium"
    }

    offer = models.ForeignKey(
        Offers, on_delete=models.CASCADE, related_name="details")
    title = models.CharField(max_length=30, blank=False, null=False)
    revisions = models.IntegerField(blank=False, null=False)
    delivery_time_in_days = models.IntegerField(blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)
    features = models.JSONField(default=list)
    offer_type = models.CharField(choices=OFFER_TYPES, max_length=12, default=BASIC)
