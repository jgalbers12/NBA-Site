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
        expected_params = {'per_mode48':'Totals', 'sort_by':None, 'asc':False}
        for k in params.keys():
            try:
                expected_params[k] = params[k]
            except KeyError:
                print(f'key error {k}')

        box = utils.Leaders(per_mode48=expected_params['per_mode48'])
        form = LeadersForm(initial={key:val for key,val in params.items()})
        box.data.sort_df_by(expected_params['sort_by'], bool(expected_params['asc']))

    else:
        box = utils.Leaders()
        form = LeadersForm()

    names = box.data.df['PLAYER']
    box.data.remove_cols(['PLAYER', 'RANK', 'TEAM_ID'])
    stats_dict = box.data.get_dict()
    name_id_stats = zip(names, stats_dict['index'], stats_dict['data'])
    cols = stats_dict['columns']
    form.fields['sort_by'].choices = zip(cols,cols)
    
    context = {
        'name_id_stats': name_id_stats,
        'cols' : cols,
        'form': form,
    }
    return render(request, 'players/leaders.html', context=context)