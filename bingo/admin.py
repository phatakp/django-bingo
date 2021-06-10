from django.contrib import admin
from .models import Player, Crossed

# Register your models here.
admin.site.register(Player)


@admin.register(Crossed)
class CrossedAdmin(admin.ModelAdmin):
    list_display = ('player', 'num_list')
