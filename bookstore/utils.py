from django.http import JsonResponse

from user.utils import JWTToken


def verify_token(function):
    def wrapper(self, request):
        if 'HTTP_AUTHORIZATION' not in request.META:
            resp = JsonResponse({'message': 'Token not provided in the header'})
            resp.status_code = 400
            return resp
        token = JWTToken().jwt_decode(request.META['HTTP_AUTHORIZATION'])

        request.data.update({'user_id':token.get('id')})
        return function(self, request)

    return wrapper
