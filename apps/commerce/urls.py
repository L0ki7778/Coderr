from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import offers_views, orders_views

router = DefaultRouter()
router.register(r'offers',offers_views.OffersViewset,basename="offers")
router.register(r'orders', orders_views.OrdersViewset, basename='orders')

urlpatterns = [
    path("",include(router.urls)),
    path("offerdetails/<int:detail_id>/", offers_views.OfferDetailView.as_view()),
    path("order-count/<int:business_user_id>/",orders_views.OrderCountView.as_view()),
    path("completed-order-count/<int:business_user_id>/",orders_views.OrderCountView.as_view())
    ]
