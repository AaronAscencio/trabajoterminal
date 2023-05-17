from django.db import models
from core.user.models import User
from django.core.validators import RegexValidator
from datetime import date


RELATIONSHIP_OPTIONS = [
    ('PAPÁ', 'PAPÁ'),
    ('MAMÁ', 'MAMÁ'),
    ('OTRO', 'OTRO'),
]

GENDER_OPTIONS = [
        ('MASCULINO', 'MASCULINO'),
        ('FEMENINO', 'FEMENINO'),
    ]

# Create your models here.
class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(verbose_name='Nombre', max_length=150, blank=False,null=False)
    paternal_surname = models.CharField(verbose_name='Apellido Paterno', max_length=150, blank=False,null=False)
    maternal_surname = models.CharField(verbose_name='Apellido Materno', max_length=150, blank=False,null=False)
    birthday_date = models.DateField(verbose_name='Fecha de Nacimiento')
    gender = models.CharField(max_length=30, choices=GENDER_OPTIONS, verbose_name='Sexo')
    relationship = models.CharField(max_length=30, choices=RELATIONSHIP_OPTIONS, verbose_name='Parentesco')
    street = models.CharField(verbose_name='Calle', max_length=100, blank=False,null=False)
    street_number = models.CharField(verbose_name='Numero', max_length=15, blank=False,null=False)
    neighborhood = models.CharField(verbose_name='Colonia', max_length=100, blank=False,null=False)
    zip = models.CharField(verbose_name='Codigo Postal', max_length=5, blank=False,null=False,validators=[RegexValidator(r'^\d{5}$', 'SOLO SE PERMITEN NUMEROS')])
    city = models.CharField(verbose_name='Municipio', max_length=100, blank=False,null=False)
    state = models.CharField(verbose_name='Estado', max_length=100, blank=False,null=False)
    telephone = models.CharField(verbose_name='Telefono', max_length=13, blank=False,null=False,unique=True)

    def get_age(self):
        today = date.today()
        age = today.year - self.birthday_date.year
        if today.month < self.birthday_date.month or (today.month == self.birthday_date.month and today.day < self.birthday_date.day):
            age -= 1
        return age

    def __str__(self):
        return f'{self.user.username} - {self.name} {self.paternal_surname} {self.maternal_surname}'
    
    def get_full_name(self):
        return f'{self.name} {self.paternal_surname} {self.maternal_surname}'
        
    class Meta:
        verbose_name = 'Tutor'
        verbose_name_plural = 'Tutores'
        ordering = ['name']