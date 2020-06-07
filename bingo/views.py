from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import PlayerForm, SearchForm
from .models import Player
from .ticketGenerator import generate_ticket
# Create your views here.


class HomeView(View):
    template_name = 'bingo/home.html'

    def get_context_data(self, *args, **kwargs):
        if 'player_form' not in kwargs:
            kwargs['player_form'] = PlayerForm(prefix='player')
        if 'search_form' not in kwargs:
            kwargs['search_form'] = SearchForm(prefix='search')
        return kwargs

    def get_object(self, username):
        try:
            player = Player.objects.get(username=username)
        except Player.DoesNotExist:
            return None
        return player

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        context = {}
        print(request.POST)
        if 'player' in request.POST:
            print('Player Form Submitted')
            player_form = PlayerForm(request.POST, prefix='player')
            if player_form.is_valid():
                username = player_form.cleaned_data.get('username')
                ticket = generate_ticket()
                new_ticket = ','.join([str(ticket[row][col])
                                       for row in range(3)
                                       for col in range(9)])
                player, created = Player.objects.update_or_create(
                    username=username, defaults={'ticket': new_ticket})
                context['ticket'] = ticket
                context['username'] = username
                context['prefix'] = 'player'
            else:
                context['player_form'] = player_form

        if 'search' in request.POST:
            search_form = SearchForm(request.POST, prefix='search')
            if search_form.is_valid():
                username = search_form.cleaned_data.get('username')
                player = self.get_object(username)
                if player:
                    ticket = player.ticket.split(',')
                    player_ticket = [ticket[row * 9:row * 9 + 9]
                                     for row in range(3)]
                    context['ticket'] = player_ticket
                    context['username'] = username
                    context['prefix'] = 'search'
                else:
                    context['error_message'] = 'No Player with Username=' + \
                        username + ' found!!'

        return render(request, self.template_name, self.get_context_data(**context))
