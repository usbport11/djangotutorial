from django.urls import path
from . import views
from django.views.generic import TemplateView
#from django.contrib.auth import views as auth_views

app_name = "dnd"
urlpatterns = [
  path("", views.MainIndexView.as_view(), name="index"),
  #path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
  #path('login/', views.MainLoginView, name='login'),
  path('login/', views.MainLoginView.as_view(), name='login'),
  #path('logout/', views.MainLogoutView.as_view(), name='logout'),
  path('logout/', views.MainLogoutView, name='logout'),

  path("hero/", views.HeroListView.as_view(), name="hero-list"),
  path("hero/<int:pk>/", views.HeroDetailView.as_view(), name="hero-detail"),
  path("hero/add", views.HeroCreateView.as_view(), name="hero-add"),
  path("hero/<int:pk>/delete", views.HeroDeleteView.as_view(), name="hero-delete"),
  path("hero/<int:pk>/edit", views.HeroUpdateView.as_view(), name="hero-edit"),

  path("scenario/", views.ScenarioListView.as_view(), name="scenario-list"),
  path("scenario/<int:pk>/", views.ScenarioDetailView.as_view(), name="scenario-detail"),
  path("scenario/add", views.ScenarioCreateView.as_view(), name="scenario-add"),
  path("scenario/<int:pk>/delete", views.ScenarioDeleteView.as_view(), name="scenario-delete"),
  path("scenario/<int:pk>/edit", views.ScenarioUpdateView.as_view(), name="scenario-edit"),

  path('cuberoll', TemplateView.as_view(template_name='cuberoll.html'), name='cuberoll'),
]
