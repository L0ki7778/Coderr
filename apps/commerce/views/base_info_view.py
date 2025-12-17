from apps.accounts.models import User
from ..models.reviews import Review
from ..models.offers import Offers
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


def get_average_rating(review_list: list[Review]):
    sum = 0
    number_of_reviews = review_list.count()
    for review in review_list if review_list else None:
        sum = sum + review.rating
    average = sum / number_of_reviews if sum else 0
    return average


class BaseInfoView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        review_count = Review.objects.all().count()
        average_rating = get_average_rating(Review.objects.all())
        offerers = User.objects.filter(type='business')
        business_profile_count = offerers.count()
        offer_count = Offers.objects.all().count()

        return Response({
            'review_count':review_count,
            'average_rating':average_rating,
            'business_profile_count':business_profile_count,
            'offer_count':offer_count
        })
