from UserService.models import User, Token, Role

class UserService:

    def create_user(self, name, email, password):
        user = User.objects.create(name=name, email=email)
        user.set_password(password)
        default_role = Role.objects.get(name="Default")
        user.roles.set([default_role])
        user.save()
        return user

    def verify_user(self, email, password):
        try:
            user = User.objects.get(email=email)
            if user.match_password(password):
                return UserService.generate_auth_token(user), None
            else:
                return None, Exception("Invalid Email or password")

        except User.DoesNotExist:
            return None, Exception("Invalid Email or password")

    @staticmethod
    def generate_auth_token(user):
        token = user.generate_auth_token()
        print(token.token)
        token.save()
        print(token.token)
        return token

    def verify_token(self, token):
        try:
            obj_token = Token.objects.get(token=token)

            if obj_token.is_valid_token():
                return obj_token
            return None
        except Token.DoesNotExist:
            return None