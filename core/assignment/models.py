from django.db import models
from core.user.models import User
# Create your models here.

class PatientGroup(models.Model):
    specialist = models.ForeignKey(User, related_name='patientgroup_specialist', on_delete=models.CASCADE, verbose_name='Especialista')
    patient = models.ForeignKey(User, related_name='patientgroup_patient', on_delete=models.CASCADE,verbose_name='Paciente')

class Assignment(models.Model):
    group = models.ForeignKey(PatientGroup, on_delete=models.CASCADE, verbose_name='Grupo')
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    publication_date = models.DateField(verbose_name='Fecha de publicación')
    due_date = models.DateField(verbose_name='Fecha límite')
    file = models.FileField(upload_to='assignments/', verbose_name='Archivo adjunto')
    submitted = models.BooleanField(verbose_name='Enviado', default=False)

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE, verbose_name='Asignacion')
    file = models.FileField(upload_to='submissions/', verbose_name='Archivo adjunto')
    



