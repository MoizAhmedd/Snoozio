from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePageView.as_view(),name = 'home'),
    path('survey/',views.SurveyView.as_view(),name = 'survey'),
    path('data/',views.SurveyDataView.as_view(),name = 'data'),
]
