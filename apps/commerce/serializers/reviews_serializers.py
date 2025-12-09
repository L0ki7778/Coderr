from ..models import reviews
from rest_framework import serializers


class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = reviews.Review
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at','reviewer']
        
    