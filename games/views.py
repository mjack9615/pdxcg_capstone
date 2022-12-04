from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy

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