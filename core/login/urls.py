from django.urls import path
from .views import *

app_name = 'login'

urlpatterns = [
    path('',DashboardView.as_view(),name='dashboard'),
    path('login/',LoginFormView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    
]