from django.db import models
from django.urls import reverse

class Game(models.Model):
    title = models.CharField(max_length=50)
    platform = models.CharField(max_length=50)
    score = models.IntegerField()

    def __str__(self):
        return f'{self.title} - {self.platform} - {self.score}'

    class Meta:
        ordering = ['-platform']

    def get_absolute_url(self):
        return reverse('games:home', args=(self.pk,))
