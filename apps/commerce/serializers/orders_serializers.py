from rest_framework import serializers
from ..models import orders


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model=orders.Orders
        exclude=["offers"]

    def create(self, validated_data):
        request = self.context.get("request")

        return super().create(validated_data)
