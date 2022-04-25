from django.urls import path

from .views.book import BookAPI
from .views.cart import CartAPI

urlpatterns = [
    path('book', BookAPI.as_view(), name='book'),
    path('cart', CartAPI.as_view(), name='cart')
]
