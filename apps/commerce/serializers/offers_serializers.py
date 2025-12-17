from ..models import offers
from rest_framework import serializers


class OfferDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = offers.Details
        exclude = ["offer"]


class SingleOfferDetailSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = offers.Details
        fields = ['id', 'url']

    def get_url(self, obj):
        return f'http://127.0.0.1:8000/api/offerdetails/{obj.id}/'


class SingleOfferSerializer(serializers.ModelSerializer):
    details = SingleOfferDetailSerializer(many=True)

    class Meta:
        model = offers.Offers
        exclude = ["user", "created_at", "updated_at"]


class OfferCreateSerializer(serializers.ModelSerializer):
    details = OfferDetailsSerializer(many=True)

    class Meta:
        model = offers.Offers

        exclude = ["user", "created_at", "updated_at"]

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        details_data = validated_data.pop("details")
        offer = offers.Offers.objects.create(user=user, **validated_data)
        for detail in details_data:
            offers.Details.objects.create(offer=offer, **detail)
        return offer

    def update(self, instance, validated_data):
        details_data = validated_data.pop('details', [])
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            instance.save()

        for detail_data in details_data:
            detail_instance = offers.Details.objects.get(
                offer=instance,
                offer_type=detail_data['offer_type']
            )

            serializer = OfferDetailsSerializer(
                detail_instance,
                data=detail_data,
                partial=True
            )

            serializer.is_valid(raise_exception=True)
            serializer.save()

        return instance
