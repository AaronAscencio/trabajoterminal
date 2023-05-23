from django.shortcuts import redirect
from datetime import datetime
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect





class RoleRequiredMixin():

    role_required = None
    def dispatch(self, request, *args, **kwargs):
        ROLES_DICT = {
        'admin': request.user.is_admin,
        'tutor': request.user.is_tutor,
        'specialist':request.user.is_specialist,
        'patient':request.user.is_patient,
        }

        if ROLES_DICT[self.role_required]:
            return super().dispatch(request, *args, **kwargs)
        if not ROLES_DICT[self.role_required]:
            messages.error(request,'No tienes los permisos necesarios')        
            return HttpResponseRedirect(reverse_lazy('login:dashboard'))