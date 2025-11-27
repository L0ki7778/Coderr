from rest_framework import viewsets, views , status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from ..serializers import offers_serializers
from ..models import offers
from rest_framework import authentication

class OffersViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = offers_serializers.OfferCreateSerializer
    queryset = offers.Offers.objects.all()


class OfferdetailView(views.APIView):
    authentication_classes: [authentication.TokenAuthentication]
    permission_classes: [AllowAny]

    def get(self, request, *args, **kwargs):
        detail = offers.Details.objects.get(id=kwargs["detail_id"])
        serializer = offers_serializers.OfferDetailsSerializer(detail)

        return Response(serializer.data) if detail else Response("Detail not found", status=status.HTTP_404_NOT_FOUND)
