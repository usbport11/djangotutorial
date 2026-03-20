from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import logout
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Scenario, Hero
from .forms import ScenarioForm, HeroForm, MainAuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView

class MainIndexView(ListView):
    template_name = "dnd/index.html"
    def get_queryset(self):
        return None

class MainLoginView(LoginView):
    authentication_form = MainAuthenticationForm
    template_name = 'login.html'

def MainLogoutView(request):
    logout(request)
    return redirect(reverse('dnd:index'))

#def MainLogoutView(LogoutView):
#    next_page = 'dnd:index'

class ScenarioDetailView(DetailView):
    model = Scenario
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ScenarioListView(LoginRequiredMixin, ListView):
    login_url = '/dnd/login/'
    redirect_field_name = 'redirect_to'
    model = Scenario
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ScenarioCreateView(CreateView):
    form_class = ScenarioForm
    model = Scenario

class ScenarioUpdateView(UpdateView):
    form_class = ScenarioForm
    model = Scenario
    template_name = "dnd/scenario_form.html"

class ScenarioDeleteView(DeleteView):
    model = Scenario
    success_url = reverse_lazy("dnd:scenario-list")

class HeroDetailView(DetailView):
    model = Hero
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class HeroListView(ListView):
    model = Hero
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class HeroCreateView(CreateView):
    form_class = HeroForm
    model = Hero

class HeroUpdateView(UpdateView):
    form_class = HeroForm
    model = Hero
    template_name = "dnd/hero_form.html"

class HeroDeleteView(DeleteView):
    model = Hero
    success_url = reverse_lazy("hero-list")
