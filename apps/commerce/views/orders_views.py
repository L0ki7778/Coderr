from rest_framework.viewsets import ModelViewSet
from rest_framework import views, generics, response
from ..permissions import IsCustomer
from ..serializers import orders_serializers
from ..models.orders import Orders
from ..models.offers import Details
from apps.accounts.models import User


class OrdersViewset(ModelViewSet):
    permission_classes = [IsCustomer]
    serializer_class = orders_serializers.OrderSerializer
    queryset = Orders.objects.all().prefetch_related('customer_user','business_user','offer_detail')

    def perform_create(self, serializer):
        offer_detail_id = self.request.data.get("offer_detail_id")
        offer_detail = Details.objects.select_related('offer__user').get(id=offer_detail_id)
        offerer = offer_detail.offer.user
        customer = self.request.user
        serializer.save(offer_detail=offer_detail, business_user=offerer,customer_user=customer)
        

class OrderCountView(views.APIView):
    
    def get(self, request,*args, **kwargs):
        path = request.path
        print(path)
        if path.startswith('/api/completed-order-count/'):
            orders = Orders.objects.filter(business_user = kwargs['business_user_id'], status = "completed")
        else:
            orders = Orders.objects.filter(business_user = kwargs['business_user_id'])
        return response.Response({  "completed_order_count": orders.count()})


# class CompletedOrderCountView(views.APIView):
    
#     def get(self, request,*args, **kwargs):
#         orders = Orders.objects.filter(business_user = kwargs['business_user_id'], status = "completed")
#         return response.Response({  "completed_order_count": orders.count()})
