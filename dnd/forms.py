from django import forms
from .models import Gender, Race, Specialization, State, Scenario

class ScenarioForm(forms.Form):
    name = forms.CharField(
      widget=forms.TextInput(attrs={'class':'block mb-2.5 text-sm font-medium text-heading'})
    )
    description = forms.CharField(
      widget=forms.TextInput(attrs={'class':'block mb-2.5 text-sm font-medium text-heading'})
    )

class HeroForm(forms.Form):
    name = forms.CharField()
    description = forms.CharField()
    history = forms.CharField()
    level = forms.IntegerField()
    age = forms.IntegerField()
    gender = forms.ModelChoiceField(queryset=Gender.objects.all())
    race = forms.ModelChoiceField(queryset=Race.objects.all())
    specialization = forms.ModelChoiceField(queryset=Specialization.objects.all())
    health = forms.IntegerField()
    mana = forms.IntegerField()
    state = forms.ModelChoiceField(queryset=State.objects.all())
    scenario = forms.ModelChoiceField(queryset=Scenario.objects.all())
