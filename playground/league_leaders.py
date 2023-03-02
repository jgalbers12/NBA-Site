from nba_api.stats.endpoints import LeagueLeaders

leaders = LeagueLeaders(scope='Rookies')
leaders_dict = leaders.get_normalized_dict()
print(leaders.expected_data)