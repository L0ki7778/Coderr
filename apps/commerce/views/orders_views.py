from rest_framework.viewsets import ModelViewSet
from rest_framework import views, response
from rest_framework.permissions import IsAuthenticated
from ..permissions import isOrdererOrOfferer
from ..serializers import orders_serializers
from ..models.orders import Orders
from ..models.offers import Details
from django.db.models import Q


def super_user_access():
    return (
        Orders.objects.select_related(
            "customer_user",
            "business_user",
            "offer_detail"
        )
    )


class OrdersViewset(ModelViewSet):
    permission_classes = [IsAuthenticated, isOrdererOrOfferer]
    serializer_class = orders_serializers.OrderSerializer

    def get_queryset(self):
        user = self.request.user
        
        if user.is_staff or user.is_superuser:
            return super_user_access()
        
        else:
            return (
            Orders.objects
            .filter(
                Q(customer_user=user) | Q(business_user=user)
            )
            .select_related(
                "customer_user",
                "business_user",
                "offer_detail"
            )
        )

    def perform_create(self, serializer):
        offer_detail_id = self.request.data.get("offer_detail_id")
        offer_detail = Details.objects.select_related(
            'offer__user').get(id=offer_detail_id)
        offerer = offer_detail.offer.user
        customer = self.request.user
        serializer.save(offer_detail=offer_detail,
                        business_user=offerer, customer_user=customer)


class OrderCountView(views.APIView):

    def get(self, request, *args, **kwargs):
        path = request.path
        print(path)
        if path.startswith('/api/completed-order-count/'):
            orders = Orders.objects.filter(
                business_user=kwargs['business_user_id'], status="completed")
            return response.Response({"completed_order_count": orders.count()})
        else:
            orders = Orders.objects.filter(
                business_user=kwargs['business_user_id'], status="in_progress")
        return response.Response({"order_count": orders.count()})
