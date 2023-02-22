from django.urls import path
from . import views

app_name = 'teams'

urlpatterns = [
    path('all_teams/',views.all_teams,name='all_teams'),
    path('team_info/<int:pk>',views.team_info,name='team_info'),
    path('standings/',views.team_standings,name='team_standings')
]
