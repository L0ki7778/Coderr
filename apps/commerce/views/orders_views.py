from rest_framework.viewsets import ModelViewSet
from permissions import IsCustomer
from ..serializers import orders_serializers
from ..models.orders import Orders
from ..models.offers import Details


class OrdersViewset(ModelViewSet):
    permission_classes = [IsCustomer]
    serializer_class =[orders_serializers.OrderSerializer]
    queryset = Orders.objects.all()

    def perform_create(self, request):
        data = request.data
        detail_id = data.get("offer_detail_id")
        detail = Details.objects.get(id=detail_id)
