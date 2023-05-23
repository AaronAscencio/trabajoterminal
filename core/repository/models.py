from django.db import models 
from core.user.models import User

# Create your models here.
class Repository(models.Model):
    specialist = models.ForeignKey(User, related_name='repository_specialist', on_delete=models.CASCADE, verbose_name='Especialista')
    patient = models.ForeignKey(User, related_name='repository_patient', on_delete=models.CASCADE,verbose_name='Paciente')

class Material(models.Model):
    repository = models.OneToOneField(Repository, on_delete=models.CASCADE, verbose_name='Repositorio')
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    file = models.FileField(upload_to='material/', verbose_name='Archivo adjunto')


