from django.test import TestCase
from unittest import TestCase as TC

from .utils import Leaders

# Create your tests here.

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

class LeadersUtilsTests(TC):

    def test_leaders_util_returns_nonempty_list(self):
        result = Leaders().data
        self.assertGreater(len(result), 0)
        self.assertEqual(type(result), type(list()))

    def test_leaders_can_sort(self):
        result = Leaders().data.sort_by(0)
        prev = result[0]
        for r in result[1:]:
            self.assertLessEqual(prev,r)
            prev = r

    def test_leaders_can_remove_cols(self):
        results = Leaders().data
        new_results = results.remove_cols(col_nums=0)
        self.assertEqual(len(results[0]) == len(new_results[0]) + 1)
        new_results = results.remove_cols(col_nums=[0,1])
        self.assertEqual(len(results[0]) == len(new_results[0]) + 2)

