from rest_framework import viewsets, views, status, filters
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Min
from ..serializers import offers_serializers
from ..models import offers
from rest_framework import authentication
from ..filters import OfferFilter


class OffersViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = offers_serializers.OfferCreateSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = OfferFilter
    ordering_fields = ['updated_at', 'min_price']
    ordering = ['updated_at']

    def get_queryset(self):
        return (offers.Offers.objects
                .prefetch_related('details')
                .annotate(min_price=Min('details__price'))
                 )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return offers_serializers.SingleOfferSerializer
        return self.serializer_class


class OfferDetailView(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        detail = offers.Details.objects.get(id=kwargs["detail_id"])
        serializer = offers_serializers.OfferDetailsSerializer(detail)

        return Response(serializer.data) if detail else Response("Detail not found", status=status.HTTP_404_NOT_FOUND)
