from django.forms import ModelForm, TextInput
from .models import Player


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ('username',)
        widgets = {'username': TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Pick a username',
                                                'id': 'name'})}


class SearchForm(ModelForm):
    class Meta:
        model = Player
        fields = ('username',)
        widgets = {'username': TextInput(attrs={'class': 'form-control',
                                                'placeholder': 'Username to Search',
                                                'id': 'name'})}
