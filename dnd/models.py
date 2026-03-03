import datetime
from django.db import models
from django.utils import timezone

class Scenario(models.Model):
  name = models.CharField(max_length=64)
  description = models.CharField(max_length=256)
  def __str__(self):
    return self.name

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
