from django import forms
from .models import League, Team, Team_Member


class LeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = ['name']
        labels = {'name': 'Name'}


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']
        labels = {'name': 'Team name'}


class Team_MemberForm(forms.ModelForm):
    class Meta:
        model = Team_Member
        fields = ['firstname', 'lastname']
        labels = {'firstname': 'First name', 'lastname': 'Last name'}
