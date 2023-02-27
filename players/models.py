from django.db import models

from teams.models import BasicTeam

class BasicPlayer(models.Model):
    id = models.IntegerField(primary_key = True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"