from nba_api.stats.static import players
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import CommonTeamRoster
from nba_api.stats.endpoints import PlayoffPicture
from nba_api.stats.endpoints import CommonPlayerInfo

KD_ID = 201142
SUNS_ID = 1610612756
SEASON_ID = 12022

def get_active_players():
    active_players = []
    for player in players.get_players():
        if player['is_active']:
            active_players.append(player)

    return(active_players)

def get_team_roster(team_id, **kwargs):
    roster = CommonTeamRoster(team_id)
    for k,v in kwargs.items():
        roster.__setattr__(k, v)
    return(roster.get_normalized_dict())

#kd = commonplayerinfo.CommonPlayerInfo(player_id = KD_ID)
#print(kd.get_normalized_dict())
#suns = get_team_roster(team_id = SUNS_ID, season_id = SEASON_ID)
#print(suns)

class Endpoint:
    def __init__(self, endpoint, proxy, headers, timeout, **kwargs):
        self.endpoint = endpoint
        self.proxy = proxy
        self.headers = headers
        self.timeout = timeout
        self.kwargs = kwargs

    def get_dict(self):
        if hasattr(self.endpoint, 'get_normalized_dict'):
            d = self.endpoint(proxy = self.proxy, headers = self.headers, timeout = self.timeout, **self.kwargs)
            return d.get_normalized_dict()
        else:
            raise Exception('Not a valid endpoint')

class TeamRoster2(Endpoint):
    def __init__(self, team_id, season=None, proxy=None, timeout=None, headers=None):
        super().__init__(CommonTeamRoster, proxy, timeout, headers, team_id = team_id, season = season)
    
    def get_players(self):
        d = self.get_dict()
        return d['CommonTeamRoster']

class TeamRoster(CommonTeamRoster):
    def __init__(self, team_id, **kwargs):
        super().__init__(team_id, **kwargs)

    def _get_team_roster_dict(self):
        roster = self.get_normalized_dict()
        return(roster)
    
    def get_players(self):
        roster = self._get_team_roster_dict()
        players = roster['CommonTeamRoster']
        return(players)
    
    def get_coaches(self):
        roster = self._get_team_roster_dict()
        coaches = roster['Coaches']
        return(coaches)

from nba_api.stats.endpoints import CommonPlayerInfo

class PlayerInfo(CommonPlayerInfo):
    def __init__(self, player_id):
        super().__init__(player_id)

    def _get_player_info_dict(self):
        player_info = self.get_normalized_dict()
        return player_info
    
    def get_bio(self):
        bio = self._get_player_info_dict()['CommonPlayerInfo'][0]
        return bio
    
    def get_bio_tags(self):
        key_list = []
        for key in self.get_bio().keys():
            key_list.append(key)
        return key_list
    
if __name__ == "__main__":
    kd = PlayerInfo(KD_ID)
    print(kd.get_bio_tags())