from rest_framework import serializers


class GetUserResponseSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=False)
    email = serializers.EmailField(required=False)
    name = serializers.CharField(max_length=100, required=False)
    response_status = serializers.CharField(max_length=50, required=False)