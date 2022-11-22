from django.db import models
from django.urls import reverse

class Game(models.Model):
    title = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)
    score = models.IntegerField()

    def get_absolute_url(self):
        return reverse('games:home', args=(self.pk,))
