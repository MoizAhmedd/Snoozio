from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.HomePageView.as_view(),name = 'home'),
    path('api/data',views.get_data,name='api-data'),
    path('api/chart/data',views.CharData.as_view(),name='api-chart-data'),
    path('survey/<int:pk>',views.SurveyView.as_view(),name = 'survey'),
    path('login/',auth_views.LoginView.as_view(redirect_authenticated_user=True),name = 'login'),
    path('signup/',views.signup,name = 'signup'),
    path('success/<int:pk>',views.SuccessView.as_view(),name = 'success'),
    path('sleeptime/',views.SleepTimeView.as_view(),name = 'sleeptime'),
    path('logout/',auth_views.LogoutView.as_view(),name = 'logout'),
    path('redirect/',views.RedirectView.as_view(),name = 'redirect'),
]
