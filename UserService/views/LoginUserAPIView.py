
from rest_framework.views import APIView
from rest_framework.response import Response
from UserService.services import UserService
from rest_framework import status
from UserService.serializer.LogInUserRequestSerializer import LogInUserRequestSerializer
from UserService.serializer.LogInUserResponseSerializer import LogInUserResponseSerializer

# Create your views here.


class LogInUserAPIView(APIView):

    def __init__(self,  **kwargs):
        super().__init__(**kwargs)
        self.user_service = UserService()

    def post(self, request):
        try:

            serialized_req = LogInUserRequestSerializer(data=request.data)
            serialized_req.is_valid(raise_exception=True)

            token, ex = self.user_service.verify_user(
                email=serialized_req.data.get("email"),
                password=serialized_req.data.get("password")
            )

            if ex:
                data = {
                    "response_status": "Login failed"
                }
                response = LogInUserResponseSerializer(data=data)
                print(ex)

                return Response(response.data, status=status.HTTP_400_BAD_REQUEST)

            data = {
                "token": str(token.token),
                "expires_at": token.expires_at,
                "response_status": "Login successful"
            }

            response = LogInUserResponseSerializer(data=data)

            response.is_valid(raise_exception=True)

            return Response(response.data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            data = {
                "response_status": "Login failed"
            }
            response = LogInUserResponseSerializer(data=data)
            response.is_valid(raise_exception=False)

            return Response(response.data, status=status.HTTP_400_BAD_REQUEST)
