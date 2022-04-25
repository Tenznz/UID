from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Book
from ..serializers import BookSerializer


class BookAPI(APIView):
    """Books operation"""

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            serializer.create(request.data)
            return Response({
                "message": "Book store successfully",
                "data": serializer.data
            }, 201)
        except ValidationError:
            return Response({
                "error_message": serializer.errors
            }, 400)
        except AssertionError:
            return Response({
                "error": "empty value"
            }, 400)
        except Exception as e:
            return Response({
                "error_message": str(e)
            }, 400)

    def get(self, request):
        try:
            books = BookSerializer(Book.objects.all(), many=True)
            return Response({
                "message": "retrieve all the books successfully",
                "data": books.data
            }, 200)
        except Exception as e:
            print(e)
            return Response({
                "message": str(e)
            }, 400)

    def delete(self, request):
        try:
            Book.objects.get(pk=request.data.get("book_id")).delete()
            return Response({
                "message": "book delete successfully !!"
            }, 204)
        except ObjectDoesNotExist:
            return Response({
                "message": "book not found"
            }, 200)
        except Exception as e:
            print(type(e))
            return Response({
                "message": str(e)
            }, 400)
