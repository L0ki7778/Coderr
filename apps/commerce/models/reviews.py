from django.db import models
from django.core.exceptions import ValidationError
from apps.accounts.models import User


class Review(models.Model):
    business_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_reviews")
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="given_reviews")
    rating = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        constraints = [
            models.CheckConstraint(condition=models.Q(rating__gte=1, rating__lte=5), name='rating_range')
        ]
    
    def clean(self):
        super().clean()
        print(self.business_user, self.reviewer)
        if self.business_user.type != 'business':
            raise ValidationError({'business_user': 'Only offerers can be reviewed.'})
        if self.reviewer.type != 'customer':
            raise ValidationError({'reviewer': 'Only customers can write reviews.'})
    