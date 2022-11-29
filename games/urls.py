from django.urls import path
from . import views

app_name = 'games'
urlpatterns = [
    path('', views.home, name='home'),
    path('games/about/', views.about, name='about'),
    path('games/results/', views.ListGames.as_view(), name='results'),
    path('games/new/', views.CreateGame.as_view(), name='new')
]