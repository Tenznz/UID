import jwt


class JWTToken:
    def jwt_encode(self, payload):
        return jwt.encode(payload, 'secret', algorithm='HS256')

    def jwt_decode(self, token):
        return jwt.decode(token, key='secret', algorithms=['HS256'])
