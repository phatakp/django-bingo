from django.db import models
from django.core.validators import int_list_validator

# Create your models here.


class Player(models.Model):
    default_ticket = ','.join('0' for n in range(27))
    username = models.CharField(max_length=50, unique=True)
    ticket = models.CharField(validators=[int_list_validator],
                              max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username


class Crossed(models.Model):
    player = models.ForeignKey(Player,
                               blank=True, null=True,
                               on_delete=models.SET_NULL)
    num_list = models.CharField(validators=[int_list_validator],
                                max_length=400, blank=True, null=True)

    def __str__(self):
        return self.player.username if self.player else 'All Random'
