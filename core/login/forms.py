from django.contrib.auth.forms import AuthenticationForm
from django import forms

class CustomAuthenticationForm(AuthenticationForm):

    def clean(self):
        cleaned_data = super().clean()
        user = self.get_user()
        if user.is_specialist and not user.active:
            raise forms.ValidationError("El administrador aún no ha verificado su cuenta, ingrese más tarde")
        return cleaned_data