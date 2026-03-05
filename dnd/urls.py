from django.urls import path
from . import views

app_name = "dnd"
urlpatterns = [
  path("", views.MainIndexView.as_view(), name="index"),

  path("hero/", views.HeroListView.as_view(), name="hero-list"),
  path("hero/<int:pk>/", views.HeroDetailView.as_view(), name="hero-detail"),
  path("hero/add", views.HeroCreateView.as_view(), name="hero-create"),
  path("hero/<int:pk>/del", views.HeroDeleteView.as_view(), name="hero-delete"),
  path("hero/<int:pk>/upd", views.HeroCreateView.as_view(), name="hero-update"),

  path("scenario/", views.ScenarioListView.as_view(), name="scenario-list"),
  path("scenario/<int:pk>/", views.ScenarioDetailView.as_view(), name="scenario-detail"),
  path("scenario/add", views.ScenarioCreateView.as_view(), name="scenario-create"),
  path("scenario/<int:pk>/del", views.ScenarioDeleteView.as_view(), name="scenario-delete"),
  path("scenario/<int:pk>/upd", views.ScenarioCreateView.as_view(), name="scenario-update"),
]
