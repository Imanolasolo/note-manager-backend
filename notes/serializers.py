from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Note

# Serializers are used to convert complex data types, such as querysets and model instances,
# into native Python datatypes that can then be easily rendered into JSON, XML, or other content types.
# They also provide deserialization, allowing parsed data to be converted back into complex types.

from django.contrib.auth.models import User
from rest_framework import serializers

# Serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    # Validate the username to ensure it is unique
    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("This username is already taken.")
        return value

# Serializer for the Note model
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created_at', 'updated_at']