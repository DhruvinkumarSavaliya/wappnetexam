from django.db import models
from django.contrib.auth.models import User# Create your models here.


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)

class Publisher(models.Model):
    name = models.CharField(max_length = 100)

class Book(models.Model):
    name = models.CharField(max_length = 100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)


    