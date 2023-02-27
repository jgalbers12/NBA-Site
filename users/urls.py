from django.urls import path,include
from .views import register_user

app_name = 'users'

urlpatterns = [
    path('register_user/', register_user, name='register'),
]
