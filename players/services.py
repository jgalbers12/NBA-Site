from .models import BasicPlayer
from .utils import get_active_players

class BasicPlayerUpdater:

    def __init__(self):
        self.active_players = get_active_players()
        self.active_players_keys = self.active_players.keys()
        self.existing_players = self._get_existing_players()
        self.existing_players_ids = self.existing_players.keys()

    def _get_existing_players(self):
        players = get_active_players()
        ids = players.keys()
        existing_objs = BasicPlayer.objects.in_bulk(ids)
        return existing_objs

    def create_players(self):
        objs = []
        for key, val in self.active_players.items():
            if not key in self.existing_players_ids:
                objs.append(BasicPlayer(id=key, **val))
        return BasicPlayer.objects.bulk_create(objs)

    def update_inactive_players(self):
        objs = []
        for key, val in self.existing_players.items():
            if not key in self.active_players_keys:
                val.is_active = False
                objs.append(val)
        return BasicPlayer.objects.bulk_update(objs=objs, fields=['is_active'])