from django.db import models
from core.user.models import User
from datetime import date


DISABILITY_OPTIONS = [
        ('DISCAPACIDAD MOTRIZ', 'DISCAPACIDAD MOTRIZ'),
        ('DISCAPACIDAD INTELECTUAL', 'DISCAPACIDAD INTELECTUAL'),
        ('AMBAS DISCAPACIDADES', 'AMBAS DISCAPACIDADES'),
    ]

GENDER_OPTIONS = [
        ('MASCULINO', 'MASCULINO'),
        ('FEMENINO', 'FEMENINO'),
    ]

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,related_name='patient_user')
    name = models.CharField(verbose_name='Nombre', max_length=150, blank=False,null=False)
    paternal_surname = models.CharField(verbose_name='Apellido Paterno', max_length=150, blank=False,null=False)
    maternal_surname = models.CharField(verbose_name='Apellido Materno', max_length=150, blank=False,null=False)
    birthday_date = models.DateField(verbose_name='Fecha de Nacimiento')
    disability_type = models.CharField(max_length=30, choices=DISABILITY_OPTIONS, verbose_name='Tipo de Discapacidad')
    gender = models.CharField(max_length=30, choices=GENDER_OPTIONS, verbose_name='Sexo')
    tutor = models.ForeignKey(User,on_delete=models.CASCADE,related_name='tutor_patients')

    def __str__(self):
        return f'{self.user.username} - {self.name} {self.paternal_surname} {self.maternal_surname}'

    def get_full_name(self):
        return f'{self.name} {self.paternal_surname} {self.maternal_surname}'
    
    def get_age(self):
        today = date.today()
        age = today.year - self.birthday_date.year
        if today.month < self.birthday_date.month or (today.month == self.birthday_date.month and today.day < self.birthday_date.day):
            age -= 1
        return age
