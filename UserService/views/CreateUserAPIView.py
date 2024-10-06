from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from UserService.services import UserService
from  UserService.serializer.CreateUserRequestSerializer import CreateUserRequestSerializer
from  UserService.serializer.CreateUserResponseSerializer import CreateUserResponseSerializer
from rest_framework import status

# Create your views here.

class CreateUserAPIView(APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_service = UserService()

    def post(self, request):
        try:
            # Get the request data
            serialized_req = CreateUserRequestSerializer(data=request.data)
            serialized_req.is_valid(raise_exception=True)

            user = self.user_service.create_user(
                email=serialized_req.data.get("email"),
                name=serialized_req.data.get("name"),
                password=serialized_req.data.get("password")
            )

            data = {
                "user_id": user.id,
                "response_status": "User created successfully"
            }

            response = CreateUserResponseSerializer(data=data)
            response.is_valid(raise_exception=True)

            return Response(response.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            data = {
                "response_status": "response_status"
            }
            response = CreateUserResponseSerializer(data=data)
            response.is_valid(raise_exception=True)

            return Response(response.data, status=status.HTTP_400_BAD_REQUEST)
