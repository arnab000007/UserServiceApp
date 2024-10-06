
from  rest_framework import serializers

class CreateUserResponseSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(required=False)
    response_status = serializers.CharField(max_length=50)