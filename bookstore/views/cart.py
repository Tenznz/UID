from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Book, Cart, CartItem
from ..serializers import CartSerializer, CartItemSerializer
from ..utils import verify_token


class CartAPI(APIView):
    """cart operation"""

    @verify_token
    def post(self, request):
        try:
            # cart
            book_list = request.data.get('book_list')
            total_price = 0
            total_quantity = sum([i.get('quantity') for i in book_list])
            for book in book_list:
                book_data = Book.objects.get(id=book.get('book_id'))
                total_price += book_data.price

            cart_data = Cart.objects.filter(user_id=request.data.get('user_id'), status=1)
            if not cart_data:
                cart_data = {
                    "total_quantity": total_quantity,
                    "total_price": total_price,
                    "user_id": request.data.get('user_id'),
                    "status": 1
                }
                serializer_cart = CartSerializer(data=cart_data)
                serializer_cart.is_valid(raise_exception=True)
                serializer_cart.save()
                cart_data = serializer_cart.data
                print(cart_data)
                cart_id = cart_data.get('id')

            else:
                cart_data = Cart.objects.get(user_id=request.data.get('user_id'), status=1)
                cart_id = cart_data.id
                cart_data.total_quantity += total_quantity
                cart_data.total_price += total_price
                cart_data.save()
            print("cart inserted")
            # cartitem
            for book in book_list:
                cart_item = {
                    'cart_id': cart_id,
                    'book_id': book.get('book_id'),
                    'user_id': request.data.get('user_id'),
                    'quantity': book.get('quantity')
                }
                cart_item_serializer = CartItemSerializer(data=cart_item)
                cart_item_serializer.is_valid(raise_exception=True)

                cart_item_serializer.save()
            return Response({
                "message": "cart added successfully"
            })

        except Exception as e:
            print(type(e))
            return Response({
                "message": str(e)
            })

    @verify_token
    def get(self, request):
        user_carts = CartItem.objects.filter(user_id=request.data.get('user_id')) \
            .select_related('cart_id') \
            .select_related('book_id')
        cart_list = list()
        total_price=0
        for cart in user_carts:
            cart_list.append({
                "book_name": cart.book_id.book_name,
                'price': cart.book_id.price,
                'quantity': cart.quantity
            })
            total_price=cart.cart_id.total_price
        return Response({
            'message': 'successfully',
            'user_id': request.data.get('user_id'),
            'cart_list': cart_list,
            'total_price':total_price
        })
