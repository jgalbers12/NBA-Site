from django.shortcuts import render
from . import models
from . import utils

# Create your views here.

def all_teams(request):
    teams = models.BasicTeam.objects.all()
    context = {
        'teams': teams
        }
    return render(request,'teams/all_teams.html',context=context)

def team_info(request, pk):
    team = models.BasicTeam.objects.get(id=pk)
    record = utils.get_team_record(pk)
    context = {
        'team' : team,
        'record': record
        }
    return render(request, 'teams/team_info.html',context=context)

def team_standings(request):
    team = models.BasicTeam.objects.all()
    standings = utils.get_standings_dict()
    context = {
        'team': team,
        'standings': standings
    }
    return render(request, 'teams/team_standings.html',context=context)
