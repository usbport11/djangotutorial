from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Scenario, Hero

class MainIndexView(generic.ListView):
  template_name = "dnd/index.html"
  def get_queryset(self):
    return None

class ScenarioListView(generic.ListView):
  template_name = "dnd/scenario_list.html"
  context_object_name = "scenario_list"
  def get_queryset(self):
    return Scenario.objects.all()

class HeroListView(generic.ListView):
  template_name = "dnd/hero_list.html"
  context_object_name = "hero_list"
  def get_queryset(self):
    return Hero.objects.all()

#def index(request):
#  scenario_list = Scenario.objects.all()
#  context = {"scenario_list": scenario_list}
#  return render(request, "dnd/index.html", context)

#def detail(request, scenario_id):
#  scenario = get_object_or_404(Scenario, pk=scenario_id)
#  return render(request, "dnd/detail.html", {"scenario": scenario})
