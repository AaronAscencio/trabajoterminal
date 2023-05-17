from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.core.validators import RegexValidator
from core.user.models import User
from .models import Specialist

GENDER_OPTIONS = [
        ('MASCULINO', 'MASCULINO'),
        ('FEMENINO', 'FEMENINO'),
    ]


class SpecialistSignUpForm(UserCreationForm):

    email = forms.EmailField(required=True)
    name = forms.CharField(label='Nombre', max_length=150, required=True)
    paternal_surname = forms.CharField(label='Apellido Paterno', max_length=150, required=True)
    maternal_surname = forms.CharField(label='Apellido Materno', max_length=150, required=True)
    professional_license = forms.CharField(label='Cedula Profesional', max_length=8, required=True, validators=[
            RegexValidator(
                regex=r'^\d{5,8}$',
                message='La cedula profesional debe tener entre 5 y 8 digitos.'
            )
        ])
    birthday_date = forms.DateField(label='Fecha de Nacimiento')
    gender = forms.CharField(max_length=30, label='Sexo', widget=forms.Select(choices=GENDER_OPTIONS))
    image = forms.ImageField(label='Imagen', required=False)
    street = forms.CharField(label='Calle', max_length=100, required=True)
    street_number = forms.CharField(label='Número', max_length=15, required=True)
    neighborhood = forms.CharField(label='Colonia', max_length=100, required=True)
    zip = forms.CharField(label='Código Postal', max_length=5, required=True, validators=[RegexValidator(r'^\d{5}$', 'El código postal debe tener 5 números')])
    city = forms.CharField(label='Municipio', max_length=100, required=True)
    state = forms.CharField(label='Estado', max_length=100, required=True)
    telephone = forms.CharField(label='Teléfono', max_length=13, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        exclude = ['active']

    @transaction.atomic
    def save(self, commit=True):
        data = {}
        user = super().save(commit=False)
        user.is_specialist = True
        user.email = self.cleaned_data['email']
        user.image = self.cleaned_data.get('image', None)
        user.save()
        specialist = Specialist(user=user)
        specialist.name = self.cleaned_data['name']
        specialist.birthday_date = self.cleaned_data['birthday_date']
        specialist.gender = self.cleaned_data['gender']
        specialist.paternal_surname = self.cleaned_data['paternal_surname']
        specialist.maternal_surname = self.cleaned_data['maternal_surname']
        specialist.professional_license = self.cleaned_data['professional_license']
        specialist.street = self.cleaned_data['street']
        specialist.street_number = self.cleaned_data['street_number']
        specialist.neighborhood = self.cleaned_data['neighborhood']
        specialist.zip = self.cleaned_data['zip']
        specialist.city = self.cleaned_data['city']
        specialist.state = self.cleaned_data['state']
        specialist.telephone = self.cleaned_data['telephone']
        specialist.save()
        return data