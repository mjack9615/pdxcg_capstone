from django.urls import path
from . import views

app_name = 'games'
urlpatterns = [
    path('', views.home, name='home'),
    path('games/about/', views.about, name='about'),
    path('games/all_games/', views.ListGames.as_view(), name='all_games'),
    path('games/new/', views.CreateGame.as_view(), name='new'),
    path('games/update/<pk>', views.UpdateGame.as_view(), name='update'), 
    path('games/delete/<pk>', views.DeleteGame.as_view(), name='delete'),
    path('games/api_kw', views.api_kw, name='api_kw'),
    path('games/api_ss', views.api_ss, name='api_ss'),
    path('games/api_tr', views.api_tr, name='api_tr')
]