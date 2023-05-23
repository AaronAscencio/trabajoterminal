from django.db import models
from core.user.models import User

# Create your models here.

class Appointment(models.Model):
    specialist = models.ForeignKey(User, related_name='appointment_specialist', on_delete=models.CASCADE, verbose_name='Especialista')
    patient = models.ForeignKey(User, related_name='appointment_patient', on_delete=models.CASCADE,verbose_name='Paciente')
    date = models.DateField(verbose_name='Fecha de la Cita')
    start_time = models.TimeField(verbose_name='Hora de inicio')
