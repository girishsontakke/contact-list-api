from django.contrib import auth
import jwt
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer, UserSerializer
from rest_framework.generics import GenericAPIView
from django.conf import settings
import datetime
# Create your views here.


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer_data = serializer.data
        user = auth.authenticate(
            username=serializer_data['username'], password=serializer_data['password'])

        if user:
            auth_token = jwt.encode(
                {"id": user.id, "username": user.username}, key=settings.SECRET_KEY, algorithm="HS256")
            serializer = UserSerializer(user)
            data = {
                "user": serializer.data,
                "token": auth_token
            }
            return Response(data=data, status=status.HTTP_202_ACCEPTED)
        return Response(data={"detail": "invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
