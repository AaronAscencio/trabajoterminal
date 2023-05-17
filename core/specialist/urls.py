from django.urls import path
from .views import *

app_name = 'specialist'

urlpatterns = [
    path('signup/',SpecialistCreateView.as_view(),name='specialist_create'),
]