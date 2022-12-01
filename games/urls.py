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
    path('games/kw_filter/', views.kw_filter, name='kw_filter'),
    path('games/plat_filter/', views.plat_filter, name='plat_filter'),
    path('games/score_filter', views.score_filter, name='score_filter'),
    path('games/score_plat_filter', views.score_plat_filter, name='score_plat_filter')
]