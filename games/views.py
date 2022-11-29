from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .models import Game

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html') 

class ListGames(ListView):
    model = Game
    template_name = 'results.html'

class CreateGame(LoginRequiredMixin, CreateView):
    model = Game
    template_name = 'new_game.html'
    fields = ['owner', 'title', 'platform', 'score']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)