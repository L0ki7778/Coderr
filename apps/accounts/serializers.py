from rest_framework import serializers
from .models import User
from typing import Any, Dict



class ResgistrationSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True, min_length=4)

    class Meta:
        model = User
        fields = ["username", "email", "password", "repeated_password", "type"]
        extra_kwargs = {"password": {'write_only':True}}


    def validate(self, attrs: Dict[str, Any])-> Dict[str, Any]:
        if attrs['password'] != attrs['repeated_password']:
            raise serializers.ValidationError('Passwörter stimmen nicht überein')
        return attrs
    
    def validate_email(self, value:str)-> str:
        if User.objects.filter(email = value).exists():
            raise serializers.ValidationError({"error":"Email wird bereits verwendet"})
        return value
    
    def create(self, validated_data: dict[str, Any])->User:
        password = validated_data.pop("password")
        validated_data.pop("repeated_password")
        
        user = User(
            username = validated_data.get('username'),
            email = validated_data.get("email")
        )
        
        user.set_password(password)
        user.save()
        return user