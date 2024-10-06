from rest_framework import  serializers

class LogInUserResponseSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255, required=False)
    expires_at = serializers.DateTimeField(required=False)
    response_status = serializers.CharField(max_length=255)