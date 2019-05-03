from django.shortcuts import render,redirect
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView
from .models import Profile
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from SnoozioApp.forms import SignUpForm,SurveyForm
from django.contrib.auth import authenticate,login
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'




class SuccessView(ListView):
    model = User
    template_name = 'success.html'
    context_object_name = 'user'

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

def survey(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Survey Complete')
    else:
        form = SurveyForm()
    
    return render(request,'survey.html',{'survey':form})

