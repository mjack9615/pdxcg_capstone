from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Game

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html') 

def api_kw(request):
    return render(request, 'api_kw.html')

def api_ss(request):
    return render(request, 'api_ss.html')

def api_tr(request):
    return render(request, 'api_tr.html')            

class ListGames(ListView):
    model = Game
    template_name = 'all_games.html'

class KeywordFilter(ListView):
    model = Game
    template_name = "kw_filter.html"

    def get_queryset(self): 
        query = self.request.GET.get("kw", default="")
        object_list = Game.objects.filter(title__contains=query)
        return object_list    

class PlatformFilter(ListView):
    model = Game
    template_name = "plat_filter.html"

    def get_queryset(self): 
        query = self.request.GET.get("plat", default="")
        object_list = Game.objects.filter(platform__exact=query)
        return object_list            

class ScoreFilter(ListView):
    model = Game
    template_name = "score_filter.html"

    def get_queryset(self): 
        query = self.request.GET.get("score", default=0)
        object_list = Game.objects.filter(score__gte=query)
        return object_list

class ScorePlatFilter(ListView):
    model = Game
    template_name = "score_plat_filter.html"

    def get_queryset(self):
        query = self.request.GET.get("plat", default="") 
        query = self.request.GET.get("plat_score", default=0)
        object_list = Game.objects.filter(Q(platform__exact=query) & Q(score__gte=query))
        return object_list
  
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