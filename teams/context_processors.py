from teams.models import BasicTeam

def every_team_renderer(request):
    return {'every_team': BasicTeam.objects.all()}