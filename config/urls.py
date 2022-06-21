
from django.contrib import admin
from django.urls import path, include
from app.views import *
from config.yasg import urlpatterns_yasg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/book-create/', BookCreateView.as_view()),
    path('api/v1/book-list/', BookListView.as_view()),
    path('api/v1/book-destroy/<int:pk>', BookDestroyView.as_view()),
    path('api/v1/base-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth-token/', include('djoser.urls.authtoken')),
] + urlpatterns_yasg
