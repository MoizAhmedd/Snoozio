from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Profile,Survey
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from SnoozioApp.forms import SignUpForm
from django.contrib.auth import authenticate,login
# Create your views here.
class HomePageView(ListView):
    model = Profile
    template_name = 'index.html'

class SurveyView(CreateView):
    model = Survey
    template_name = 'survey.html'
    fields = '__all__'

class SurveyDataView(ListView):
    model = Survey
    template_name = 'data.html'

class SuccessView(ListView):
    model = User
    template_name = 'success.html'

class RedirectView(ListView):
    model = User
    template_name = 'redirect.html'

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username,password=raw_password)
            login(request,user)
            return redirect('/')

    else:
        form = SignUpForm()

    return render(request,'registration/signup.html',{'form':form})
