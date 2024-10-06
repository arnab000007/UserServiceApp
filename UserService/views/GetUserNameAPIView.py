from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from UserService.serializer.GetUserResponseSerializer import GetUserResponseSerializer
from UserService.serializer.GetUserRequestSerializer import GetUserRequestSerializer
from UserService.services import UserService
from rest_framework.permissions import IsAuthenticated



class GetUserNameAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_service = UserService()

    def get(self, request):
        user = request.user
        user_info = {
            'user_name': user.name,
            'email': user.email,
            # Add any other fields you want to return
        }
        return Response({
            'message': 'This is a secured endpoint!',
            'user_info': user_info
        })

class GetUserNamePostAPIView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_service = UserService()

    def post(self, request):
        try:
            # Get the request data
            serialized_req = GetUserRequestSerializer(data=request.data)
            serialized_req.is_valid(raise_exception=True)

            token = self.user_service.verify_token(serialized_req.data.get("user_token"))

            if token is None:
                data = {
                    "response_status": "Either Token is invalid or expired"
                }
                response = GetUserResponseSerializer(data=data)
                response.is_valid(raise_exception=True)

                return Response(response.data, status=status.HTTP_400_BAD_REQUEST)

            data = {
                "user_id": token.user.id,
                "email": token.user.email,
                "name": token.user.name,
                "response_status": "User name fetched successfully"
            }

            response = GetUserResponseSerializer(data=data)
            response.is_valid(raise_exception=True)

            return Response(response.data, status=status.HTTP_200_OK)

        except Exception as e:
            data = {
                "response_status": "Something went wrong"
            }
            response = GetUserResponseSerializer(data=data)
            response.is_valid(raise_exception=True)

            return Response(response.data, status=status.HTTP_400_BAD_REQUEST)