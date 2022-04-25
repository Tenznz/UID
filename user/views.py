import logging
from datetime import datetime

from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from .email import Email
from .models import User

from .serializers import UserSerializer
from .utils import JWTToken

logging.basicConfig(filename="views.log", filemode="w")


class UserSignUp(APIView):
    """User Registration"""

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            Email().send_email(serializer.data)
            serializer.create(request.data)
            print(serializer.data.get('email'))
            return Response({
                "message": "User add successfully !!",
                "data": serializer.data
            }, 201)
        except ValidationError:
            return Response(serializer.errors)

        except Exception as e:
            return Response({
                "error_message": str(e)
            }, 400)

    def get(self, request):
        try:
            users = User.objects.get(username=request.data.get("username"))
            serializer = UserSerializer(users)
            return Response({
                "message": "users",
                "data": serializer.data
            })
        except ObjectDoesNotExist:
            return Response({
                "message": "user not found"
            }, 200)

        except Exception as e:
            return Response({
                "error_message": str(e)
            }, 400)


class UserSignIn(APIView):
    def post(self, request):
        try:
            user = auth.authenticate(username=request.data.get('username'), password=request.data.get('password'))
            print(user)
            if not user:
                return Response({
                    "message": "user not found"
                })
            user.last_login = datetime.now()
            user.save()

            return Response({
                "message": "user sign in successfully !!"
            }, 200)

        except Exception as e:
            return Response({
                "error_message": str(e)
            })

    def get(self, request, token):
        serializer = UserSerializer(JWTToken().jwt_decode(token))
        return Response({
            "message": "validation successfully",
            "data": serializer.data
        }, 200)
