from rest_framework import authentication, exceptions
import jwt
from django.conf import settings
from django.contrib.auth.models import User


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_data = authentication.get_authorization_header(request)
        if not auth_data:
            return None
        prefix, token = auth_data.decode('utf-8').split(" ")
        try:
            payload = jwt.decode(
                jwt=token, key=settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload.get("id"))
            return (user, token)
        except jwt.DecodeError as ex:
            raise exceptions.ValidationError("can not validate user")
        except jwt.ExpiredSignatureError as ex:
            raise exceptions.ValidationError(
                "token is expired request another token")
