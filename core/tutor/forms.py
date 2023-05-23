from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User,Tutor

GENDER_OPTIONS = [
        ('MASCULINO', 'MASCULINO'),
        ('FEMENINO', 'FEMENINO'),
        ('OTRO','OTRO')
    ]

RELATIONSHIP_OPTIONS = [
    ('PAPÁ', 'PAPÁ'),
    ('MAMÁ', 'MAMÁ'),
    ('OTRO', 'OTRO'),
]


class TutorSignUpForm(UserCreationForm):

    name = forms.CharField(label='Nombre', max_length=150, required=True)
    paternal_surname = forms.CharField(label='Apellido Paterno', max_length=150, required=True)
    maternal_surname = forms.CharField(label='Apellido Materno', max_length=150, required=True)
    birthday_date = forms.DateField(label='Fecha de Nacimiento')
    gender = forms.CharField(max_length=30, label='Sexo', widget=forms.Select(choices=GENDER_OPTIONS))
    relationship = forms.CharField(max_length=30, label='Parentesco', widget=forms.Select(choices=RELATIONSHIP_OPTIONS))
    image = forms.ImageField(label='Imagen', required=False)
    street = forms.CharField(label='Calle', max_length=100, required=True)
    street_number = forms.CharField(label='Número', max_length=15, required=True)
    neighborhood = forms.CharField(label='Colonia', max_length=100, required=True)
    zip = forms.CharField(label='Código Postal', max_length=5, required=True)
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
        user.is_tutor = True
        user.image = self.cleaned_data.get('image', None)
        user.save()
        tutor = Tutor(user=user)
        tutor.name = self.cleaned_data['name']
        tutor.paternal_surname = self.cleaned_data['paternal_surname']
        tutor.maternal_surname = self.cleaned_data['maternal_surname']
        tutor.relationship = self.changed_data['relationship']
        tutor.birthday_date = self.cleaned_data['birthday_date']
        tutor.gender = self.cleaned_data['gender']
        tutor.street = self.cleaned_data['street']
        tutor.street_number = self.cleaned_data['street_number']
        tutor.neighborhood = self.cleaned_data['neighborhood']
        tutor.zip = self.cleaned_data['zip']
        tutor.city = self.cleaned_data['city']
        tutor.state = self.cleaned_data['state']
        tutor.telephone = self.cleaned_data['telephone']
        tutor.save()
        return data