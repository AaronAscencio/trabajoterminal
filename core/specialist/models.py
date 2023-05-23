from django.db import models
from core.user.models import User
from django.forms.models import model_to_dict
from django.core.validators import RegexValidator,MaxLengthValidator
from datetime import date
# Create your models here.
GENDER_OPTIONS = [
        ('MASCULINO', 'MASCULINO'),
        ('FEMENINO', 'FEMENINO'),
        ('OTRO','OTRO')
    ]

class Specialist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(verbose_name='Nombre', max_length=150, blank=False,null=False)
    paternal_surname = models.CharField(verbose_name='Apellido Paterno', max_length=150, blank=False,null=False)
    maternal_surname = models.CharField(verbose_name='Apellido Materno', max_length=150, blank=False,null=False)
    gender = models.CharField(max_length=30, choices=GENDER_OPTIONS, verbose_name='Sexo')
    birthday_date = models.DateField(verbose_name='Fecha de Nacimiento')
    professional_license = models.CharField(verbose_name='Cedula Profesional',max_length=8,blank=False,null=False,unique=True,validators=[RegexValidator(r'^\d{5,8}$', 'La cedula profesional debe tener entre 5 y 8 digitos.')])
    school = models.CharField(verbose_name='Escuela de Procedencia', max_length=150, blank=False, null= False)
    year_of_graduation = models.CharField(verbose_name='Año de Egreso', max_length=4,  blank=False, null= False)
    years_of_experience = models.IntegerField(verbose_name='Años de Experiencia', blank=False, null= False)
    street = models.CharField(verbose_name='Calle', max_length=100, blank=False,null=False)
    street_number = models.CharField(verbose_name='Numero', max_length=15, blank=False,null=False)
    neighborhood = models.CharField(verbose_name='Colonia', max_length=100, blank=False,null=False)
    zip = models.CharField(verbose_name='Codigo Postal', max_length=5, blank=False,null=False,validators=[RegexValidator(r'^\d{5}$', 'SOLO SE PERMITEN NUMEROS')])
    city = models.CharField(verbose_name='Municipio', max_length=100, blank=False,null=False)
    state = models.CharField(verbose_name='Estado', max_length=100, blank=False,null=False)
    telephone = models.CharField(verbose_name='Telefono', max_length=13, blank=False,null=False,unique=True)


    def __str__(self):
        return f'{self.user.username} - {self.name} {self.paternal_surname} {self.maternal_surname}'

    def get_full_name(self):
        return f'{self.name} {self.paternal_surname} {self.maternal_surname}'
        
    class Meta:
        verbose_name = 'Especialista'
        verbose_name_plural = 'Especialistas'
        ordering = ['name']
    
    def get_age(self):
        today = date.today()
        age = today.year - self.birthday_date.year
        if today.month < self.birthday_date.month or (today.month == self.birthday_date.month and today.day < self.birthday_date.day):
            age -= 1
        return age
