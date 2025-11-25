from ..models import offers
from rest_framework import serializers

class OfferDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=offers.Details
        exclude=["offer"]

class OfferCreateSerializer(serializers.ModelSerializer):
    details = OfferDetailsSerializer(many=True)
    
    class Meta:
        model = offers.Offers
        
        exclude = ["user","created_at", "updated_at"]
        
    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        details_data = validated_data.pop("details")
        offer = offers.Offers.objects.create(user=user, **validated_data)
        for detail in details_data:
            offers.Details.objects.create(offer=offer, **detail)
        return offer
        
        
    