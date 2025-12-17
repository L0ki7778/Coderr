from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.commerce.serializers.reviews_serializers import ReviewSerializer
from apps.commerce.models.reviews import Review
from apps.accounts.models import User
from ..permissions import IsCustomer
from ..filters import ReviewFilter
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ReviewListCreateView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated, IsCustomer]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ReviewFilter
    ordering_fields = ['updated_at', 'rating']
    ordering=['updated_at']

    def create(self, request, *args, **kwargs):
        # region create
        buisiness_user = User.objects.get(id=request.data.get("business_user"))
        review = Review.objects.create(
            business_user=buisiness_user,
            reviewer=self.request.user,
            rating=request.data.get("rating"),
            description=request.data.get("description")
        )
        # endregion 
        serializer = self.get_serializer(review)
        return Response(serializer.data)


class ReviewPatchDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsCustomer]
    
