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
        try: # theres definitly a better way to do this ?
            permode = params['per_mode48']
        except KeyError:
            permode = 'Total'
        except Exception as e:
            print(e)
        try:
            sort_by = params['sort_by']
        except KeyError:
            sort_by = None
        except Exception as e:
            print(e)
        box = utils.Leaders(per_mode48=permode)
        form = LeadersForm(initial={key:val for key,val in params.items()})
        box.data.sort_df_by(sort_by)
    else:
        box = utils.Leaders()
        form = LeadersForm()
    ids = box.data.df['PLAYER_ID']
    box.data.remove_cols(['PLAYER_ID', 'TEAM_ID'])
    stats_dict = box.data.get_dict()
    stats = stats_dict['data']
    cols = stats_dict['columns']
    form.fields['sort_by'].choices = zip(cols,cols)
    context = {
        'stats': stats,
        'cols' : cols,
        'form': form,
        'ids': ids,
    }
    return render(request, 'players/leaders.html', context=context)