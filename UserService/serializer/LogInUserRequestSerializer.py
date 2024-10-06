
from  rest_framework import serializers

class LogInUserRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50)