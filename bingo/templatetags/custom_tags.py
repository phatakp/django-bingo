from django import template
from bingo.models import Crossed

register = template.Library()


@register.filter
def present(value, user=None):

    num_list = []
    if user:
        playerrand = Crossed.objects.filter(player__username=user)
        if playerrand:
            num_list = playerrand[0].num_list.split(',')
    else:
        allrand = Crossed.objects.filter(player__isnull=True)
        if allrand:
            num_list = allrand[0].num_list.split(',')
    return value in num_list
