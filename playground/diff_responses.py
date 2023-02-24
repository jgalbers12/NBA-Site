from nba_api.stats.endpoints import commonplayerinfo
import json

lbj = commonplayerinfo.CommonPlayerInfo(player_id=2544)

#print(f"normalized json \n {lbj.get_normalized_json()} \n")
#print(f"json \n {lbj.get_json()} \n")
print(f"dict \n {lbj.get_normalized_dict()} \n")
