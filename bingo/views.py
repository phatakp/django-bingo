from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.http import JsonResponse, HttpResponse
from .forms import PlayerForm, SearchForm
from .models import Crossed, Player
from .ticketGenerator import generate_ticket
# Create your views here.


class HomeView(FormView):
    template_name = 'bingo/home.html'
    form_class = PlayerForm

    def form_valid(self, form):
        form.save()
        return redirect('bingo:ticket', username=form.instance.username)


class TicketView(TemplateView):
    template_name = 'bingo/ticket.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        player = Player.objects.get(username=context['username'])
        if not player.ticket:
            ticket = generate_ticket()
            new_ticket = ','.join([str(ticket[row][col])
                                   for row in range(3)
                                   for col in range(9)])
            player.ticket = new_ticket
            player.save()
            context['ticket'] = ticket
        else:
            ticket_nums = player.ticket.split(',')
            ticket = [[ticket_nums[row*9+col]
                       for col in range(9)] for row in range(3)]
            context['ticket'] = ticket
        context['prefix'] = 'player'

        return context


class SearchView(ListView):
    model = Crossed
    template_name = 'bingo/admin.html'
    context_object_name = 'crosslist'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        username = self.request.GET.get('users', None)
        if username:
            player = Player.objects.get(username=username)
            ticket = player.ticket.split(',')
            player_ticket = [ticket[row * 9:row * 9 + 9]
                             for row in range(3)]
            context['ticket'] = player_ticket
            context['username'] = username

        numgen = [[str(row*10+col)
                   for col in range(1, 11)]
                  for row in range(9)]
        context['numgen'] = numgen

        return context


def user_json_data(request):
    term = request.GET.get('term', None)
    data = ['** No such users **']
    if term:
        qs = Player.objects.filter(username__icontains=term)
        if qs:
            data = [q.username for q in qs]

    return JsonResponse(data, safe=False)


def add_num_to_db(request):
    num = request.POST.get('num')
    username = request.POST.get('player')
    action = request.POST.get('action')

    if username:
        player = Player.objects.get(username=username)
        if Crossed.objects.filter(player=player).exists():
            playercrossed = Crossed.objects.filter(player=player).first()
            if action == 'add':
                playercrossed.num_list += f"{num},"
            else:
                num_list = playercrossed.num_list.split(',')
                num_list.remove(num)
                playercrossed.num_list = ','.join(num_list)
            playercrossed.save()
        elif action == 'add':
            Crossed.objects.create(player=player,
                                   num_list=f"{num},")
    else:
        if Crossed.objects.filter(player__isnull=True).exists():
            allcrossed = Crossed.objects.filter(player__isnull=True).first()
            allcrossed.num_list += f"{num},"
            allcrossed.save()
        else:
            Crossed.objects.create(player=None,
                                   num_list=f"{num},")
    return JsonResponse({'message': 'Success'})


def reset_game(request):
    Player.objects.all().delete()
    Crossed.objects.all().delete()

    return redirect('bingo:staff')
