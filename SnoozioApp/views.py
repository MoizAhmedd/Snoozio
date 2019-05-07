from django.shortcuts import render,redirect
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView,UpdateView
from .models import Profile,SleepTimes
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from SnoozioApp.forms import SignUpForm,SurveyForm
from django.contrib.auth import authenticate,login
# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

class SuccessView(ListView):
    model = Profile
    template_name = 'success.html'
    context_object_name = 'profile'
    def get_context_data(self,**kwargs):
        ctx = super(SuccessView,self).get_context_data(**kwargs)
        ctx['sleeptime'] = SleepTimes.objects.all()
        return ctx

class RedirectView(ListView):
    model = User
    template_name = 'redirect.html'

class SurveyView(UpdateView):
    model = Profile
    template_name = 'survey.html'
    fields = ['age','work_time','exercise_time','calories']

class SleepTimeView(CreateView):
    model = SleepTimes
    template_name = 'sleeptime.html'
    fields = '__all__'

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



