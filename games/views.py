from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template import loader

from .models import Game

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html') 

class ListGames(ListView):
    model = Game
    template_name = 'all_games.html'

class CreateGame(LoginRequiredMixin, CreateView):
    model = Game
    template_name = 'new_game.html'
    fields = ['title', 'platform', 'score']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('games:all_games')    

class UpdateGame(LoginRequiredMixin, UpdateView):
    model = Game
    template_name = 'update.html'
    fields = ['title', 'platform', 'score']

    success_url = reverse_lazy('games:all_games')

class DeleteGame(LoginRequiredMixin, DeleteView):
    model = Game
    template_name = 'delete.html'
    fields = ['title', 'platform', 'score']

    success_url = reverse_lazy('games:all_games')

def kw_filter(request):
        results = Game.objects.filter(title__contains='mario').values()
        template = loader.get_template('kw_filter.html')
        context = {
            'results': results,
        }
        return HttpResponse(template.render(context, request))

def plat_filter(request):
        results = Game.objects.filter(platform__exact='xsx').values()
        template = loader.get_template('plat_filter.html')
        context = {
            'results': results,
        }
        return HttpResponse(template.render(context, request))

def score_filter(request):
        results = Game.objects.filter(score__gte='90').values()
        template = loader.get_template('score_filter.html')
        context = {
            'results': results,
        }
        return HttpResponse(template.render(context, request))

def score_plat_filter(request):
        results = Game.objects.filter(platform__exact='win', score__gte='90').values()
        template = loader.get_template('score_plat_filter.html')
        context = {
            'results': results,
        }
        return HttpResponse(template.render(context, request))       