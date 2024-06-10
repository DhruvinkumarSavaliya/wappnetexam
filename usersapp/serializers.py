from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Author, Book, Publisher

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)

    def validate_username(self, value):
        user = User.objects.filter(username = value).first()
        if user is None:
            raise serializers.ValidationError("user not exist")
        return value


class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
    



class BookSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    publisher = serializers.PrimaryKeyRelatedField(queryset=Publisher.objects.all())

    class Meta:
        model = Book
        fields = ['name', 'author', "publisher"]

class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Author
        fields = ['name', 'user']






class PublisherSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)

    class Meta:
        model = Publisher
        fields = ['name']