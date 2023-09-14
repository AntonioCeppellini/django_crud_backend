from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User


#####model serializer for article#####
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'description'],

#####model serializer for registration#####
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {
            'write_only': True, #####we want to keep it secret
            'required': True #####we want it to be required
        }}
    #####new users creation#####
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.object.create(user = user)
        return user


