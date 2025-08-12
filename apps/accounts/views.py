from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ResgistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.permissions import AllowAny
from rest_framework import status
# from django.contrib.auth import get_user_model


# User = get_user_model()

class RegistrationView(APIView):
    permission_classes = [AllowAny]
    def post(self, request: Request) -> Response:
        serializer = ResgistrationSerializer(data=request.data)
        if serializer.is_valid():
            saved_account = serializer.save()
            username = getattr(saved_account, "username", None)
            type = getattr(saved_account, "type", None)
            email = getattr(saved_account, "email", None)
            token = Token.objects.create(user=saved_account)
            response_data = {
                "token": token.key,
                "username": username,
                "type":type,
                "email":email
                
            }
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(response_data)
