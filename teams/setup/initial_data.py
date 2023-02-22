from nba_api.stats.static import teams
from teams.models import BasicTeam
from pathlib import Path
from django.core.files import File
from nba_site.settings import BASE_DIR

def fill_basic_teams():
    # run in django shell to get basic data for teams
    nba_teams = teams.get_teams()
    for team in nba_teams:
        BasicTeam.objects.update_or_create(
            id = team['id'],
            full_name = team['full_name'],
            abb = team['abbreviation'],
            nickname = team['nickname'],
            city = team['city'],
            state = team['state']
        )

def add_logo_to_basic_model():
    all_teams = BasicTeam.objects.all()
    path = Path(BASE_DIR, 'logos/')
    for team in all_teams:
        nickname = team.nickname
        path = Path(BASE_DIR, f'logos/{nickname.lower()}.png')
        with path.open(mode='rb') as f:
            team.logo = File(f, name=path)
            team.save()

def team_dict():
    # run in django shell to get basic data for teams
    nba_teams = teams.get_teams()
    td = {}
    for team in nba_teams:
        td[team['full_name']] = team['id']
    return td

def print_teams():
    nba_teams = teams.get_teams()
    for team in nba_teams:
        print(team['full_name'])
