from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguestandings
from nba_api.stats.endpoints import CommonTeamRoster

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



class TeamRoster(CommonTeamRoster):
    def __init__(self, team_id, **kwargs):
        super().__init__(team_id, **kwargs)

    def _get_team_roster_dict(self):
        """
        returns a dict, 
        players found at return_dict['CommonTeamRoster'],
        couches found at return_dict['Coaches']
        """
        roster = self.get_normalized_dict()
        return(roster)
    
    def get_players(self):
        """ 
        returns a dict, 
        player keys: 'TeamID', 'SEASON', 'LeagueID', 'PLAYER', 'NICKNAME',
        'PLAYER_SLUG', 'NUM', 'POSITION', 'HEIGHT', 'WEIGHT', 'BIRTH_DATE',
        'AGE', 'EXP', 'SCHOOL', 'PLAYER_ID', 'HOW_ACQUIRED'
        """
        roster = self._get_team_roster_dict()
        players = roster['CommonTeamRoster']
        return(players)
    
    def get_coaches(self):
        roster = self._get_team_roster_dict()
        coaches = roster['Coaches']
        return(coaches)
    


    
