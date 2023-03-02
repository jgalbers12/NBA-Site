from django.db import models

# Create your models here.

class BasicTeam(models.Model):
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=30)
    abb = models.CharField(max_length=3)
    nickname = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='images/logos', default='images/logos/_NBA_logo.png')

    def __str__(self):
        return f"{self.full_name}"