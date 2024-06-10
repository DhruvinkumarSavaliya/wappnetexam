from django.shortcuts import render
from django_filters import rest_framework as filters
# Create your views here.
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializers import LoginSerializer, UserRegistrationSerializer, BookSerializer, AuthorSerializer, PublisherSerializer
from .models import Book, Publisher, Author
import io
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.response import Response


@api_view(['POST'])
def login_user(request):
    login_serializer = LoginSerializer(data=request.data)
    if login_serializer.is_valid():
        username = login_serializer.validated_data.get('username')
        password = login_serializer.validated_data.get('password')
        user = User.objects.filter(username = username).first()
        if user.check_password(password):
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'email': user.email
            })
    Response({
        "message": "Invalid username and passoword"
    })

@api_view(['POST'])
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = User.objects.create(username = username, password = password)
        return Response({
            'user_id': user.pk,
            'username': user.username
        })
    print(serializer.errors)
    return Response({
        "message": "Username already in use"
    },status = status.HTTP_400_BAD_REQUEST)


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

   

class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [filters.DjangoFilterBackend]


class PublisherView(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

@api_view(['GET'])
def top_author(request):
    authors = Author.objects.raw("SELECT usersapp_author.id, usersapp_author.name FROM usersapp_book inner JOIN usersapp_author ON usersapp_book.author_id = usersapp_author.id GROUP BY usersapp_author.id ORDER BY COUNT(usersapp_book.id) DESC")
    serializer = AuthorSerializer(authors, many=True)    
    return Response({
        "message": serializer.data
    })
