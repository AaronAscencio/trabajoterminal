from django.urls import path
from .views import *

app_name = 'tutor'

urlpatterns = [
    path('signup/',TutorCreateView.as_view(),name='tutor_create'),
]