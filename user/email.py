from django.core.mail import send_mail


class Email:
    def send_email(self, user):

        return send_mail(
            "welcome", f"hi {user.get('first_name')},\nwelcome to my app ",
            user.get("email"), ['dhugkar95@gmail.com'],
            fail_silently=False)
