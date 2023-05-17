from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from .models import User


# Create your views here.

'''
class SpecialistSignUpView(CreateView):
    model = User
    form_class = SpecialistSignUpForm
    template_name = 'specialist/create.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login:login')
'''
