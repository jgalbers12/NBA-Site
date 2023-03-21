from django.test import TestCase
from unittest import TestCase as TC

import pandas as pd

from .utils import Leaders, StatsTable

class PlayerLeadersTests(TestCase):

    def test_uses_correct_template(self):
        response = self.client.get('/players/leaders/')
        self.assertTemplateUsed(response, 'players/leaders.html')

    def test_can_select_mode(self):
        response = self.client.get('/players/leaders/', data={'per_mode48':'Totals'}, follow=True)
        self.assertContains(response, 'selected>Totals')
        response = self.client.get('/players/leaders/', data={'per_mode48':'PerGame'})
        self.assertContains(response, 'selected>Per Game')
        response = self.client.get('/players/leaders/', data={'per_mode48':'Per48'})
        self.assertContains(response, 'selected>Per 48')

    def test_template_receives_and_displays_data(self):
        response = self.client.get('/players/leaders/')
        data = list(response.context['name_id_stats'])
        self.assertGreater(len(data), 1)
        self.assertContains(response, '<td>')

    def test_template_has_rank_col(self):
        response = self.client.get('/players/leaders/')
        self.assertContains(response, '<th>RANK')

    def test_template_contains_links_to_player_info(self):
        response = self.client.get('/players/leaders/')
        num = len(list(response.context['name_id_stats']))
        self.assertContains(response, 'href="player_info/"', count=num)

    def test_view_processes_parameters(self):
        response = self.client.get('/players/leaders/', data={'per_mode48':'Totals',
                                                              'asc':True,
                                                              'sort_by':'GP'})
        self.assertEqual(response.status_code, 200)


class LeadersUtilsTests(TC):

    def test_leaders_util_returns_StatsTable(self):
        result = Leaders().data
        self.assertTrue(isinstance(result, StatsTable))

    def test_leaders_can_sort(self):
        data = Leaders().data
        data.sort_df_by(data.df.columns[0])
        self.assertTrue(data.df[data.df.columns[0]].is_monotonic_decreasing)

    def test_leaders_can_remove_cols(self):
        data = Leaders().data
        num_cols = len(data.df.columns)
        data.remove_cols(col_names=[data.df.columns[1]])
        self.assertEqual(len(data.df.columns), num_cols - 1)

    def test_leaders_get_dict_returns_nonempty_dict(self):
        data = Leaders().data
        data_dict = data.get_dict()
        self.assertTrue(isinstance(data_dict, dict))
        self.assertTrue(len(data_dict['data']) > 0)

    def test_leaders_uses_correct_index(self):
        data = Leaders().data
        data_dict = data.get_dict()
        indices = data_dict['index']
        for i in indices:
            self.assertRegex(str(i), r'[0-9]+')