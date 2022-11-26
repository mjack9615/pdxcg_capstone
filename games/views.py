from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Game

class ListGames(ListView):
    model = Game
    template_name = 'home.html'

class CreateGame(LoginRequiredMixin, CreateView):
    model = Game
    template_name = 'new_game.html'
    fields = ['owner', 'title', 'platform', 'score']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)