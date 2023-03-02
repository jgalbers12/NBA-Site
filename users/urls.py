from django.urls import path,include
from .views import register_user, user_profile

app_name = 'users'

urlpatterns = [
    path('register_user/', register_user, name='register'),
    path('user_profile/', user_profile, name='user_profile')
]
