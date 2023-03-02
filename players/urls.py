from django.urls import path
from . import views

app_name = 'players'

urlpatterns = [
    path('player_info/<int:id>', views.player_info, name='player_info'),
    path('leaders', views.player_leaders, name='leaders'),
]
