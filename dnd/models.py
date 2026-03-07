import datetime
from django.db import models
from django.utils import timezone
from django.forms import ModelForm

class Scenario(models.Model):
  name = models.CharField(max_length=64)
  description = models.CharField(max_length=256)
  def __str__(self):
    return self.name
  def get_absolute_url(self):
        return reverse("scenario-detail", kwargs={"pk": self.pk})

class Map(models.Model):
  name = models.CharField(max_length=64)
  description = models.CharField(max_length=256)
  scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
  def __str__(self):
    return self.name

class Place(models.Model):
  name = models.CharField(max_length=64)
  description = models.CharField(max_length=256)
  map = models.ForeignKey(Map, on_delete=models.CASCADE)
  def __str__(self):
    return self.name

class Building(models.Model):
  name = models.CharField(max_length=64)
  description = models.CharField(max_length=256)
  place = models.ForeignKey(Place, on_delete=models.CASCADE)
  def __str__(self):
    return self.name

class State(models.Model):
  name = models.CharField(max_length=64)
  def __str__(self):
    return self.name

class Gender(models.Model):
  name = models.CharField(max_length=64)
  def __str__(self):
    return self.name

class Race(models.Model):
  name = models.CharField(max_length=64)
  def __str__(self):
    return self.name

class Specialization(models.Model):
  name = models.CharField(max_length=64)
  def __str__(self):
    return self.name

class Hero(models.Model):
  name = models.CharField(max_length=64)
  description = models.CharField(max_length=256)
  history = models.CharField(max_length=1024)
#  level = models.IntegerField()
  age = models.IntegerField()
  gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
  race = models.ForeignKey(Race, on_delete=models.CASCADE)
  specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
  health = models.IntegerField()
  mana = models.IntegerField()
  state = models.ForeignKey(State, on_delete=models.CASCADE)
  scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
  def __str__(self):
    return self.name
  def get_absolute_url(self):
    return reverse('hero-detail', kwargs={'pk': self.pk})

#new
#class Inventory(models.Model):
#  hero = models.ForeignKey(Hero, on_delete=models.CASCADE)

#class Doll():
#  hero = models.ForeignKey(Hero, on_delete=models.CASCADE)
#  head = models.ForeignKey(Item, on_delete=models.CASCAD, blank=True)
#  torso = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True)
#  left_hand = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True)
#  right_hand = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True)
#  feet = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True)

#class Item(models.Model):
#  name = models.CharField(max_length=64)
#  item_type = models.ForeignKey(Inventory, on_delete=models.CASCADE)
#  inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE, blank=True)
