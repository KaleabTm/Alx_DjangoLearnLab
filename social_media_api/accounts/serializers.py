from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    followers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    following = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'bio', 'profile_picture', 'followers', 'following']
        read_only_fields = ['followers', 'following']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'bio', 'profile_picture']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            password=validated_data.pop('password'),
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        Token.objects.create(user=user)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
