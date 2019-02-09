from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Profile,Survey
# Create your views here.
class HomePageView(ListView):
    model = Profile
    template_name = 'index.html'

class SurveyView(CreateView):
    model = Survey
    template_name = 'survey.html'
    fields = '__all__'
