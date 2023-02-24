from django.shortcuts import render
from . import utils

# Create your views here.

def player_info(request, id):
    info = utils.PlayerInfo(id)
    bio_data = info.get_bio()
    stats = info.get_headline_stats()
    context = {
        'bio': bio_data,
        'stats': stats
    }
    return render(request, 'players/player_info.html', context=context)