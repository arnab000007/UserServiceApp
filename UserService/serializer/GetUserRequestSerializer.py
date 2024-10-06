from rest_framework import serializers


class GetUserRequestSerializer(serializers.Serializer):
    user_token = serializers.CharField(max_length=255)

