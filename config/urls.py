
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/book-create/', BookCreateView.as_view()),
    path('api/v1/book-list/', BookListView.as_view()),
    path('api/v1/book-destroy/<int:pk>', BookDestroyView.as_view()),
]
