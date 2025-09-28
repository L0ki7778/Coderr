from rest_framework import serializers
from typing import Any, Dict
from .models import User
from django.contrib.auth import authenticate


class RegistrationSerializer(serializers.ModelSerializer):
    repeated_password = serializers.CharField(write_only=True)
    email = serializers.EmailField(required=True, min_length=4)

    class Meta:
        model = User
        fields = ["username", "email", "password", "repeated_password", "type"]
        extra_kwargs = {"password": {'write_only': True}}

    def validate(self, attrs: Dict[str, Any]) -> Dict[str, Any]:
        if attrs['password'] != attrs['repeated_password']:
            raise serializers.ValidationError(
                'Passwörter stimmen nicht überein')
        return attrs

    def validate_email(self, value: str) -> str:
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                {"error": "Email wird bereits verwendet"})
        return value

    def create(self, validated_data: dict[str, Any]) -> User:
        first_name=''
        last_name=''
        password = validated_data.pop("password")
        if len(validated_data.get('username').split(' '))>1:
            first_name, last_name = validated_data.get('username').split(' ')
        elif len(validated_data.get('username').split('_')) > 1:
            first_name, last_name = validated_data.get('username').split('_')

        user = User(
            username=validated_data.get('username'),
            email=validated_data.get("email"),
            first_name=first_name,
            last_name=last_name,
            type=validated_data.get('type'),
        )

        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(
            username=data.get("username"),
            password=data.get("password")
        )
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        data["user"] = user
        return data


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ["user", "username", "first_name", "last_name", "file", "location",
                  "tel", "description", "working_hours", "type", "email", "created_at"]

    def get_user(self, obj):
        return obj.pk
