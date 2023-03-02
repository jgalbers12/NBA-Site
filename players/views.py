from django.shortcuts import render

from . import utils
from .forms import LeadersForm


def player_info(request, id):
    info = utils.PlayerInfo(id)
    bio_data = info.get_bio()
    stats = info.get_headline_stats()
    context = {
        'bio': bio_data,
        'stats': stats
    }
    return render(request, 'players/player_info.html', context=context)

def player_leaders(request):
    if request.GET:
        params = request.GET
        kwargs = {key:params[key] for key in request.GET if key != 'csrfmiddlewaretoken'} # replace this
        box = utils.Leaders(**kwargs) # requires form fields align with __init__ params
        form = LeadersForm(initial=kwargs)
    else:
        box = utils.Leaders()
        form = LeadersForm()
    stats = box.data
    cols = stats[0].keys()
    context = {
        'stats': stats,
        'cols': cols,
        'form': form,
    }
    return render(request, 'players/leaders.html', context=context)