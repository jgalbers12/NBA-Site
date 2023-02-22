from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguestandings

ALL_TEAMS = teams.get_teams()

def get_standings_dict():
    standings = leaguestandings.LeagueStandings().get_dict()
    standings_dict_list = [dict(zip(standings['resultSets'][0]['headers'],standings['resultSets'][0]['rowSet'][i])) for i in range(len(ALL_TEAMS))]
    return standings_dict_list

def get_team_record(team_id=None):
    standings_dict_list = get_standings_dict()
    for team in standings_dict_list:
        if team_id == team['TeamID']:
            return team['Record']
    raise Exception("team_id is not a valid team id")
