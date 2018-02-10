from time import timezone

from rest_framework import serializers
from django.contrib.auth.models import User
from starnavi.models import Post, Like_Unlike


class StarnaviSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author_id', 'title', 'text', 'like', 'dislike', 'created_date')
#        read_only_fields = ('id', 'author_id', 'like', 'dislike', 'created_date',)


class UserSerializer(serializers.ModelSerializer):
    #posts = serializers.PrimaryKeyRelatedField(many=True)
    class Meta:
        model = User
        fields = ('__all__')

class Like_UnlikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like_Unlike
        fields = ('post_id', 'value', 'login_id', 'created_date')

class RegistrationSerializer(serializers.ModelSerializer):
    """Serializers registration requests and creates a new user."""
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        user = super(RegistrationSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
