from django.db import models
from django.core.validators import int_list_validator

# Create your models here.


class Player(models.Model):
    default_ticket = ','.join('0' for n in range(27))
    username = models.CharField(max_length=50)
    ticket = models.CharField(validators=[int_list_validator],
                              max_length=100,
                              default=default_ticket)

    def __str__(self):
        return self.username
