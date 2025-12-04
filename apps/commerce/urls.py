from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import offers_views

router = DefaultRouter()
router.register(r'offers',offers_views.OffersViewset,basename="offers")

urlpatterns = [
    path("",include(router.urls)),
    path("offerdetails/<int:detail_id>/", offers_views.OfferDetailView.as_view())
    ]
