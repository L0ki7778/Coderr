from rest_framework import serializers
from ..models import orders


class OrderSerializer(serializers.ModelSerializer):
    # Flatten offer_detail fields
    title = serializers.CharField(source='offer_detail.title', read_only=True)
    revisions = serializers.IntegerField(source='offer_detail.revisions', read_only=True)
    delivery_time_in_days = serializers.IntegerField(source='offer_detail.delivery_time_in_days', read_only=True)
    price = serializers.IntegerField(source='offer_detail.price', read_only=True)
    features = serializers.JSONField(source='offer_detail.features', read_only=True)
    offer_type = serializers.CharField(source='offer_detail.offer_type', read_only=True)
    
    class Meta:
        model = orders.Orders
        read_only_fields = [
            'customer_user', 'business_user'
        ]
        exclude=['offer_detail']

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == "status":
                setattr(instance,attr,value)
                instance.save()
        return instance