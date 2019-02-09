from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile
# Create your views here.
class HomePageView(ListView):
    model = Profile
    template_name = 'index.html'
