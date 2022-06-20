from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

class Book(models.Model):
    title = models.CharField(max_length=222)
    author = models.CharField(max_length=222)
    profile = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    JANR = (
        ('Художественная', 'Художественная'),
        ('Техческая', 'Техческая'),
        ('Детская', 'Детская'),
    )
    genre = models.CharField(max_length=222, choices=JANR)


