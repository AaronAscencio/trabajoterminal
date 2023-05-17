from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.core.validators import RegexValidator
from core.user.models import User
from .models import Patient

DISABILITY_OPTIONS = [
        ('DISCAPACIDAD MOTRIZ', 'DISCAPACIDAD MOTRIZ'),
        ('DISCAPACIDAD INTELECTUAL', 'DISCAPACIDAD INTELECTUAL'),
        ('AMBAS DISCAPACIDADES', 'AMBAS DISCAPACIDADES'),
    ]

GENDER_OPTIONS = [
        ('MASCULINO', 'MASCULINO'),
        ('FEMENINO', 'FEMENINO'),
    ]


class PatientSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    name = forms.CharField(label='Nombre', max_length=150, required=True)
    paternal_surname = forms.CharField(label='Apellido Paterno', max_length=150, required=True)
    maternal_surname = forms.CharField(label='Apellido Materno', max_length=150, required=True)
    birthday_date = forms.DateField(label='Fecha de Nacimiento')
    disability_type = forms.CharField(max_length=30, label='Tipo de Discapacidad', widget=forms.Select(choices=DISABILITY_OPTIONS))
    gender = forms.CharField(max_length=30, label='Sexo', widget=forms.Select(choices=GENDER_OPTIONS))
    image = forms.ImageField(label='Imagen', required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        exclude = ['active']
    
    @transaction.atomic
    def save(self,tutor, commit=True):
        data = {}
        user = super().save(commit=False)
        user.is_patient = True
        user.email = self.cleaned_data['email']
        user.image = self.cleaned_data.get('image', None)
        user.save()
        patient = Patient(user=user)
        patient.name = self.cleaned_data['name']
        patient.paternal_surname = self.cleaned_data['paternal_surname']
        patient.maternal_surname = self.cleaned_data['maternal_surname']
        patient.birthday_date = self.cleaned_data['birthday_date']
        patient.disability_type = self.cleaned_data['disability_type']
        patient.gender = self.cleaned_data['gender']
        patient.tutor = tutor
        patient.save()
        return data