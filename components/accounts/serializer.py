from rest_framework import serializers

from .models import User

class UserSerializer(serializers.Serializer):

    email       = serializers.EmailField(max_length=255 )
    first_name  = serializers.CharField(max_length=12)
    last_name   = serializers.CharField(max_length=12)
    username    = serializers.CharField(max_length=15)
    is_active      = serializers.BooleanField()
    is_staff       = serializers.BooleanField()
    timestamp   = serializers.DateTimeField()

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)