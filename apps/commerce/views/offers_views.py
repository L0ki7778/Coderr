from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from ..serializers import offers_serializers
from ..models import offers


class OffersViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = offers_serializers.OfferCreateSerializer
    queryset = offers.Offers.objects.all()
    
   
    
