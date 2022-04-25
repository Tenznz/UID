from django.urls import path
from .views import UserSignUp, UserSignIn

urlpatterns = [
    path("signup", UserSignUp.as_view(), name='signup'),
    path("signin", UserSignIn.as_view(), name='signin'),
    path("validate/<str:token>", UserSignIn.as_view(), name='validation')
]
