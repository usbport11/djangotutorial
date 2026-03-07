from django import forms
from .models import Gender, Race, Specialization, State, Scenario, Hero

class ScenarioForm(forms.ModelForm):
    class Meta:
        model = Scenario
        fields = ['name', 'description']
        class_input = """
          w-full rounded-sm border 
	  border-neutral-300 bg-neutral-50 px-2 py-2 text-sm focus-visible:outline-2 
	  focus-visible:outline-offset-2 focus-visible:outline-black disabled:cursor-not-allowed 
	  disabled:opacity-75 dark:border-neutral-700 dark:bg-neutral-900/50 dark:focus-visible:outline-white
        """
        widgets = {
            'name': forms.TextInput(attrs={'class':class_input}),
            'description': forms.TextInput(attrs={'class':class_input})
        }

class HeroForm(forms.ModelForm):
    class_input = """
        w-full rounded-sm border
        border-neutral-300 bg-neutral-50 px-2 py-2 text-sm focus-visible:outline-2
        focus-visible:outline-offset-2 focus-visible:outline-black disabled:cursor-not-allowed
        disabled:opacity-75 dark:border-neutral-700 dark:bg-neutral-900/50 dark:focus-visible:outline-white
    """
    gender = forms.ModelChoiceField(queryset=Gender.objects.all(),
      widget=forms.Select(attrs={'class': class_input}))
    race = forms.ModelChoiceField(queryset=Race.objects.all(),
      widget=forms.Select(attrs={'class': class_input}))
    specialization = forms.ModelChoiceField(queryset=Specialization.objects.all(),
      widget=forms.Select(attrs={'class': class_input}))
    state = forms.ModelChoiceField(queryset=State.objects.all(),
      widget=forms.Select(attrs={'class': class_input}))
    scenario = forms.ModelChoiceField(queryset=Scenario.objects.all(),
      widget=forms.Select(attrs={'class': class_input}))
    class Meta:
        model = Hero
        fields = ["name", "description", "history", "age", "gender", "race", "specialization", "health", "mana", "state", "scenario"]
        class_input = """
          w-full rounded-sm border
          border-neutral-300 bg-neutral-50 px-2 py-2 text-sm focus-visible:outline-2
          focus-visible:outline-offset-2 focus-visible:outline-black disabled:cursor-not-allowed
          disabled:opacity-75 dark:border-neutral-700 dark:bg-neutral-900/50 dark:focus-visible:outline-white
        """
        widgets = {
            'name': forms.TextInput(attrs={'class':class_input}),
            'description': forms.TextInput(attrs={'class':class_input}),
            'history': forms.TextInput(attrs={'class':class_input}),
            'age': forms.TextInput(attrs={'class':class_input}),
            'health': forms.TextInput(attrs={'class':class_input}),
            'mana': forms.TextInput(attrs={'class':class_input}),
        }
