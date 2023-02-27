from django.db import models
from django.contrib.auth.models import User

from teams.models import BasicTeam

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False, primary_key=True)
    favorite_team = models.ForeignKey(BasicTeam, on_delete=models.SET_NULL, null=True)