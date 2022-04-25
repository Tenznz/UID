from rest_framework import serializers

from .models import Book, Cart, CartItem


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["book_name", "author", "price"]

    def create(self, validate):
        """

        :param validate:
        :return: bookdata
        """
        return Book.objects.create(**validate)


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"

    def create(self, validate):
        """

        :param validate:
        :return: cart data
        """
        print(validate)
        print(type(validate))
        return Cart.objects.create(**validate)


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = "__all__"

    def create(self, validate):
        """

        :param validate:
        :return: cart data
        """
        return CartItem.objects.create(**validate)
