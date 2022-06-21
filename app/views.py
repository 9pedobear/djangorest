from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class BookCreateView(generics.CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)

class BookListView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = (IsAuthenticated, )

class BookDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    permission_classes = (IsOwner, IsAuthenticated)