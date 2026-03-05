from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Scenario, Hero
from .forms import ScenarioForm, HeroForm

class MainIndexView(ListView):
  template_name = "dnd/index.html"
  def get_queryset(self):
    return None

class ScenarioDetailView(DetailView):
    model = Scenario
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ScenarioListView(ListView):
    model = Scenario
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ScenarioFormView(FormView):
    template_name = "scenario.html"
    form_class = ScenarioForm
    def form_valid(self, form):
        return super().form_valid(form)

class ScenarioCreateView(CreateView):
    model = Scenario
    fields = ["name", "description"]

class ScenarioDeleteView(DeleteView):
    model = Scenario
    success_url = reverse_lazy("scenario-list")

class HeroDetailView(DetailView):
    model = Hero
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class HeroListView(ListView):
    model = Hero
    paginate_by = 100
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class HeroFormView(FormView):
    template_name = "hero.html"
    form_class = HeroForm
    def form_valid(self, form):
        return super().form_valid(form)

class HeroCreateView(CreateView):
    model = Hero
    fields = ["name", "description", "history", "age", "gender", "race", "specialization", "health", "mana", "state", "scenario"]

class HeroDeleteView(DeleteView):
    model = Hero
    success_url = reverse_lazy("hero-list")
