from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=100, min_length=8)
    first_name = serializers.CharField(max_length=100, min_length=2)
    last_name = serializers.CharField(max_length=100, min_length=2)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]

    def validate(self, attrs):
        if not attrs['email']:
            raise serializers.ValidationError(
                {"email": ("EmailField is required")})
        if User.objects.filter(email=attrs["email"]).exists():
            raise serializers.ValidationError(
                {"email", ("Email Already in use")})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ["username", "password"]
