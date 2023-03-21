from nba_api.stats.endpoints import CommonPlayerInfo
from nba_api.stats.endpoints import LeagueLeaders
from nba_api.stats.static import players
import pandas as pd

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
        
        
class Leaders:

    def __init__(self, per_mode48='Totals'):
        self.endpoint = LeagueLeaders(per_mode48 = per_mode48)
        self.data = StatsTable(self.endpoint.get_data_frames()[0])


class StatsTable:

    def __init__(self, df:pd.DataFrame):
        self.df = df.set_index('PLAYER_ID')

    def remove_cols(self, col_names):
        if isinstance(col_names, list):
            try:
                new_df = self.df.drop(col_names, axis=1)
                self.df = new_df
            except Exception as e:
                print(e)
        else:
            raise Exception("remove_cols takes a list of col_names")
        
    def sort_df_by(self, col_name, ascending=False):
        if col_name in self.df.columns:
            self.df = self.df.sort_values(by=[col_name], ascending=ascending)
        elif not col_name:
            pass
        else:
            raise Exception('not a valid column name')
        
    def get_dict(self):
        """
        returns dict like {'index':[], 'columns':[], 'data':[]}
        """
        return self.df.to_dict('split')

