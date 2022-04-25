
import jwt


class JWTToken:
    def jwt_encode(self, payload):
        print(payload)
        return jwt.encode({"id": payload.id}, 'secret', algorithm='HS256')

    def jwt_decode(self, token):
        return jwt.decode(token, key='secret', algorithms=['HS256'])
