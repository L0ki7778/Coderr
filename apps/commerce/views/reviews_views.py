from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from apps.commerce.serializers.reviews_serializers import ReviewSerializer
from apps.commerce.models.reviews import Review
from apps.accounts.models import User
from ..permissions import IsCustomer
from rest_framework.response import Response


class ReviewListCreateView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def create(self, request, *args, **kwargs):
        # region create
        requested_buisiness_user = request.data.get("business_user")
        buisiness_user = User.objects.get(id=requested_buisiness_user)
        if not buisiness_user.type == "offerer" or self.request.user.type == "offerer":
            return Response({'Invalid': 'only customers can review offerers only.'}, status=403)
        elif buisiness_user.type == 'offerer' and self.request.user.type == "customer":
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
    
