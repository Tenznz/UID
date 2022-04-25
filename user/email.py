from django.core.mail import send_mail

from .utils import JWTToken


class Email:
    def send_email(self, user):

        return send_mail(
            "welcome", f"hi {user.get('first_name')},\nwelcome to my app "
                       f"\nclick here => http://127.0.0.1:8000/user/validate/{JWTToken().jwt_encode(user)}",
            user.get("email"), ['dhugkar95@gmail.com'],
            fail_silently=False)
