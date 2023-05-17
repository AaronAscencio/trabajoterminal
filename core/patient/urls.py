from django.urls import path
from .views import *

app_name = 'pacient'

urlpatterns = [
    path('signup/',PatientCreateView.as_view(),name='pacient_create'),
]