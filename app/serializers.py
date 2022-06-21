from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    profile = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Book
        fields = ('title', 'author', 'content', 'genre', 'profile')

class BookSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'content', )