from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Profile(models.Model):
    name = models.TextField()

class Survey(models.Model):
    name = models.CharField(max_length = 50,help_text = "What is your name?",blank=True)
    age = models.IntegerField()
    exercise = models.IntegerField(help_text = 'How Many Hours a week do you exercise?')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
