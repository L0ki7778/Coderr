from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import offers_views, orders_views, reviews_views, base_info_view

router = DefaultRouter()
router.register(r'offers',offers_views.OffersViewset,basename="offers")
router.register(r'orders', orders_views.OrdersViewset, basename='orders')

urlpatterns = [
    path("",include(router.urls)),
    path("offerdetails/<int:detail_id>/", offers_views.OfferDetailView.as_view()),
    path("order-count/<int:business_user_id>/",orders_views.OrderCountView.as_view()),
    path("completed-order-count/<int:business_user_id>/",orders_views.OrderCountView.as_view()),
    path("reviews/", reviews_views.ReviewListCreateView.as_view()),
    path("reviews/<int:pk>", reviews_views.ReviewPatchDeleteView.as_view()),
    path("base-info/", base_info_view.BaseInfoView.as_view())
    ]
