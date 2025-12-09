from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from apps.commerce.serializers.reviews_serializers import ReviewSerializer
from apps.commerce.models.reviews import Review
from ..permissions import IsCustomer


class ReviewListCreateView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        business_user = self.get
        serializer.save(reviewer=self.request.user)
    

class ReviewPatchDeleteView(GenericAPIView,DestroyModelMixin,UpdateModelMixin):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer