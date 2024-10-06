from rest_framework import authentication
from rest_framework import exceptions
from UserService.models import Token, User


class UserAuthentication(authentication.TokenAuthentication):
    def authenticate(self, request):
        secret_token = request.headers.get('Authorization')
        print(secret_token)

        if not secret_token:
            return None

        try:
            token_type, token_key = secret_token.split(' ')
            if token_type != 'Bearer':
                raise exceptions.AuthenticationFailed('Invalid token prefix.')

            token_obj = Token.objects.get(token=token_key)
            if token_obj.is_valid_token():
                return (token_obj.user, None)

        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed('Unauthorized')

        raise exceptions.AuthenticationFailed('Unauthorized')
