from django.db import models
from user.models import User


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.IntegerField()


class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    total_quantity = models.IntegerField()
    total_price = models.IntegerField()
    status = models.IntegerField()


class CartItem(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
