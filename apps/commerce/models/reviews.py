from django.db import models
from django.core.exceptions import ValidationError
from apps.accounts.models import User

def validate_user_factory(type:str):
    def validate_user(user:User):
        if user.type != type:
            raise ValidationError({'error':'only business user can be reviewed from customers only.'})
    return validate_user

class Review(models.Model):
    
    class Meta:
        constraints = [
            models.CheckConstraint(condition=models.Q(rating__gte=1, rating__lte=5), name='rating_range')
        ]    
    
    business_user = models.ForeignKey(User, on_delete=models.CASCADE, validators=[validate_user_factory('offerer')])
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, validators=[validate_user_factory('customer')])
    rating= models.IntegerField()
    description = models.TextField()
    created_at=models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    