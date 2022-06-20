from rest_framework import generics
from .serializers import BookSerializer
from .models import Book


class BookCreateView(generics.CreateAPIView):
    serializer_class = BookSerializer

class BookListView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class BookDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()