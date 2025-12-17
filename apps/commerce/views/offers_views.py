from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets, views, status, filters
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Min
from ..serializers import offers_serializers
from ..models import offers
from ..filters import OfferFilter
from ..permissions import IsOfferer


class OfferPagination(PageNumberPagination):
    page_size = 2
    max_page_size = 5
    page_size_query_param = 'page_size'


class OffersViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated,IsOfferer]
    serializer_class = offers_serializers.OfferCreateSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_class = OfferFilter
    search_fields = ['title', 'description']
    ordering_fields = ['updated_at', 'min_price']
    ordering = ['updated_at']
    pagination_class = OfferPagination
    
    def get_permissions(self):
        if self.action in ['list']:
            permission_classes = [AllowAny]
        elif self.action in ['retrieve']:
            permission_classes = [IsAuthenticated]
        elif self.action in ['create','update']:
            permission_classes = [IsOfferer]
        return [permission() for permission in permission_classes]

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
    permission_classes = [IsAuthenticated,IsOfferer]

    def get(self, request, *args, **kwargs):
        detail = offers.Details.objects.get(id=kwargs["detail_id"])
        serializer = offers_serializers.OfferDetailsSerializer(detail)

        return Response(serializer.data) if detail else Response("Detail not found", status=status.HTTP_404_NOT_FOUND)
