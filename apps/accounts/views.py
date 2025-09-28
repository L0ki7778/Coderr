from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import RegistrationSerializer, LoginSerializer, ProfileSerializer
from rest_framework.authtoken.models import Token
from rest_framework.request import Request
from rest_framework.permissions import AllowAny
from rest_framework import status
from .models import User


class RegistrationView(APIView):
    permission_classes = [AllowAny]
    def post(self, request: Request) -> Response:
        serializer = RegistrationSerializer(data=request.data)
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
    
class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request:Request)-> Response:
        serializer = LoginSerializer(data = request.data)
        
        data = {}
        if serializer.is_valid():
            saved_account: User = serializer.validated_data['user']
            token: Token = Token.objects.get(user=saved_account)
            data = {
                'token': token.key,
                'username': f'{saved_account.username}',
                'email': saved_account.email,
                'user_id': saved_account.pk
            }
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data)


class ProfileViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = ProfileSerializer

