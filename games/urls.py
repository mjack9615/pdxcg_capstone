from django.urls import path
from . import views

app_name = 'games'
urlpatterns = [
    path('', views.ListGames.as_view(), name='home'),
    path('games/new/', views.CreateGame.as_view(), name='new'),
    path('games/<int:pk>/', views.ListGames.as_view(), name='home'),
]