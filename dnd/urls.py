from django.urls import path
from . import views

app_name = "dnd"
urlpatterns = [
  path("", views.MainIndexView.as_view(), name="index"),
  #path("<int:scenario_id>/", views.ScenarioListView.as_view(), name="detail"),
  path("scenario/", views.ScenarioListView.as_view(), name="scenario_list"),
  path("hero/", views.HeroListView.as_view(), name="hero_list"),
]
