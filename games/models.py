from django.db import models
from django.urls import reverse

class Game(models.Model):
    owner = models.ForeignKey('auth.User', related_name='games', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    score = models.IntegerField()

    def __str__(self):
        return f'{self.title} - {self.platform} - {self.score}'

    class Meta:
        ordering = ['platform', 'title']

    def get_absolute_url(self):
        return reverse('games:home', args=(self.pk,))
