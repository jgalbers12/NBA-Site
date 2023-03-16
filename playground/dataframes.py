from nba_api.stats.endpoints import LeagueLeaders
import pandas as pd

df = LeagueLeaders().get_data_frames()
pd.DataFrame().drop()
print(df[0].drop)