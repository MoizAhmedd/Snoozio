from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.HomePageView.as_view(),name = 'home'),
    path('survey/',views.SurveyView.as_view(),name = 'survey'),
    path('data/',views.SurveyDataView.as_view(),name = 'data'),
    path('/login',auth_views.LoginView.as_view(redirect_authenticated_user=True),name = 'login'),
    path('signup/',views.signup,name = 'signup'),
    path('success/',views.SuccessView.as_view(),name = 'success'),
    path('logout/',auth_views.LogoutView.as_view(),name = 'logout'),
    path('redirect/',views.RedirectView.as_view(),name = 'redirect'),
]
