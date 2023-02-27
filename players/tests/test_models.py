import pytest
from django.test import Client

from players.models import BasicPlayer
from players.services import BasicPlayerUpdater
from players.utils import get_active_players

@pytest.mark.django_db
def test_create_players_returns_all_players(client:Client):
    updater = BasicPlayerUpdater()
    objs = updater.create_players()
    active_player_keys = get_active_players().keys()
    for obj in objs:
        assert (obj.id in active_player_keys)