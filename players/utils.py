from nba_api.stats.endpoints import CommonPlayerInfo
from nba_api.stats.endpoints import LeagueLeaders
from nba_api.stats.static import players

def get_active_players():
    active_players = {}
    for player in players.get_players():
        if player['is_active']:
            active_players[player['id']] = {'first_name':player['first_name'], 'last_name':player['last_name'], 'is_active':True}

    return(active_players)

class PlayerInfo(CommonPlayerInfo):
    def __init__(self, player_id):
        super().__init__(player_id)

    def _get_player_info_dict(self):
        player_info = self.get_normalized_dict()
        return player_info
    
    def get_bio(self):
        """
        returns dict with player info
        keys: 'PERSON_ID', 'FIRST_NAME', 'LAST_NAME', 'DISPLAY_FIRST_LAST', 'DISPLAY_LAST_COMMA_FIRST', 
        'DISPLAY_FI_LAST', 'PLAYER_SLUG', 'BIRTHDATE', 'SCHOOL', 'COUNTRY', 'LAST_AFFILIATION', 'HEIGHT', 
        'WEIGHT', 'SEASON_EXP', 'JERSEY', 'POSITION', 'ROSTERSTATUS', 'GAMES_PLAYED_CURRENT_SEASON_FLAG',
        'TEAM_ID', 'TEAM_NAME', 'TEAM_ABBREVIATION', 'TEAM_CODE', 'TEAM_CITY', 'PLAYERCODE', 'FROM_YEAR', 
        'TO_YEAR', 'DLEAGUE_FLAG', 'NBA_FLAG', 'GAMES_PLAYED_FLAG', 'DRAFT_YEAR', 'DRAFT_ROUND', 'DRAFT_NUMBER', 
        'GREATEST_75_FLAG'
        """
        all_info = self._get_player_info_dict()
        bio = all_info['CommonPlayerInfo'][0]
        return bio
    
    def get_headline_stats(self):
        all_info = self._get_player_info_dict()
        try:
            stats = all_info['PlayerHeadlineStats'][0]
            return stats
        except:
            return None
        
class Leaders(LeagueLeaders):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.data = TableData(self.get_data_frames()[0])
        self.data = self.get_normalized_dict()['LeagueLeaders']
        self.col_names = self.expected_data['LeagueLeaders']

class TableData:

    def __init__(self, data, cols):
        self.data = data
        self.cols = cols

    def remove_cols(self, col_nums=None, col_names=None):
        if col_nums:
            if isinstance(col_nums, int) and col_nums < len(self.cols):
                new_data = [x]



    
    

