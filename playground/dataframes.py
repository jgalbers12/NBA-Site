from nba_api.stats.endpoints import LeagueLeaders
import pandas as pd

df = LeagueLeaders().get_data_frames()[0]
print(df.columns)