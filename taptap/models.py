from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.




class Taptap(models.Model):
    player = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    score =  models.IntegerField(default=0) # models.TimeField(null=True, blank=True) #assume minutes
    understand=models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return "Score for {}".format(self.player)


class TapHighestScore(models.Model):
    player = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    score =  models.IntegerField(default=0) # models.TimeField(null=True, blank=True) #assume minutes
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    phone_number = models.CharField(max_length=13,default='')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return "Score for {} with phonenumber {} on {}".format(self.player,self.phone_number,self.timestamp)


class TapActivePlayer(models.Model):
    player_tap = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,default="",related_name="tap_player")
    player_num = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "{} Player".format(self.player_tap)


class TapStatisticPlayer(models.Model):
    player_tap = models.CharField(max_length=100)
    player_num = models.CharField(max_length=13,default='')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "{} Player".format(self.player_tap)


class BonusPoint(models.Model):
    player = models.CharField(max_length=100,default="")
    list_numbers =  models.TextField(default="") # models.TimeField(null=True, blank=True) #assume minutes
    bonus_points=models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __str__(self):
        return "Bonus point for {} is {}".format(self.player,self.bonus_points)