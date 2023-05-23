from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView,LogoutView
from .forms import CustomAuthenticationForm
from core.specialist.models import Specialist
from core.tutor.models import Tutor
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class LoginFormView(LoginView):
    template_name = 'login/login.html'
    authentication_form = CustomAuthenticationForm


    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('login:dashboard')
        return super().dispatch(request, *args, **kwargs)
    
class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = 'dashboard.html'


    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['fullname'] = ''
        try:
            if self.request.user.is_specialist:
                specialist = Specialist.objects.get(user = self.request.user)
                context['fullname'] = specialist.get_full_name()
            if self.request.user.is_tutor:
                tutor = Tutor.objects.get(user = self.request.user)
                context['fullname'] = tutor.get_full_name()
        except Exception as e:
            pass
        return context