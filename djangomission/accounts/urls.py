from django.urls import path, include
from . import views
from rest_framework import urls
from accounts.views import UserCreate


urlpatterns = [
    path('signup/', UserCreate.as_view()),
    path('api-auth/', include('rest_framework.urls')),
 ]