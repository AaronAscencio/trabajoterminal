from django.forms.models import model_to_dict
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,FormView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .models import Tutor
from .forms import TutorSignUpForm
from django.shortcuts import redirect

# Create your views here.

class TutorCreateView(CreateView):
    model = Tutor
    form_class = TutorSignUpForm
    template_name = 'tutor/create.html'
    success_url = reverse_lazy('login:login')

    def get_context_data(self,**kwargs):
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Registro de un Tutor'
        context['entity'] = 'Tutor'
        context['list_url'] = reverse_lazy('login:login')
        context['action'] = 'add'
        return context


    def dispatch(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            return redirect('login:dashboard')
        return super().dispatch(request, *args, **kwargs)
    

    def post(self,request,*args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if(action=='add'):
                form = self.get_form()
                if (form.is_valid()):
                    form.save()
                else:
                    data['error'] = form.errors
            else:
                data['error'] = 'No se ha enviado ninguna accion'
        except Exception as e:
            data['error'] = str(e)
            
        return JsonResponse(data)