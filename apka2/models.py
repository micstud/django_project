from django.db import models
from django.conf import settings

class Team(models.Model):

    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bpk = models.IntegerField()
    stow = models.IntegerField()
    start_time = models.DateTimeField()
    finish_time = models.DateTimeField()

def points(bpk, stow):
    points = (-90*bpk) + (-25*stow)
    return points

def add(self):
    self.points = points(self.bpk, self.stow)
    self.save()

def __str__(self):
    return self.name
    