from django.shortcuts import render,redirect
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView,UpdateView
from .models import Profile,SleepTimes
from django.db.models import Sum,F,Func
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from SnoozioApp.forms import SignUpForm,SurveyForm
from django.contrib.auth import authenticate,login
from django.http import JsonResponse

from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

class ChartView(TemplateView):
    template_name = 'chart.html'

class SuccessView(ListView):
    model = Profile
    template_name = 'success.html'
    context_object_name = 'profile'

    for sleeptime in SleepTimes.objects.all():
        print(sleeptime.total_sleep,type(sleeptime.total_sleep))
    
    def get_context_data(self,**kwargs):
        ctx = super(SuccessView,self).get_context_data(**kwargs)
        ctx['sleeptime'] = SleepTimes.objects.all()
        return ctx

def get_data(request,*args,**kwargs):
    data = {
        "me":100
    }
    return JsonResponse(data)

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        labels = ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        sleeptimes = {}
        for sleeptime in SleepTimes.objects.all():
            if sleeptime.user.username not in sleeptimes:
                sleeptimes[sleeptime.user.username] = [sleeptime.total_sleep]
            else:
                sleeptimes[sleeptime.user.username].append(sleeptime.total_sleep)
            
        return Response(sleeptimes)
        

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



