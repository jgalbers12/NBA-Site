from django import forms


class LeadersForm(forms.Form):

    PER_MODE_CHOICES = (
        ('Totals', 'Totals'), 
        ('PerGame', 'Per Game'), 
        ('Per48', 'Per 48 Minutes')
    )

    per_mode48 = forms.ChoiceField(choices=PER_MODE_CHOICES, label='Per Mode')
    sort_by = forms.ChoiceField(required=False, label='Sort By', initial='PTS')
    asc = forms.BooleanField(required=False)
