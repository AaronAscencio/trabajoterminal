# Generated by Django 4.2 on 2023-05-17 03:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='patient_user', serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('paternal_surname', models.CharField(max_length=150, verbose_name='Apellido Paterno')),
                ('maternal_surname', models.CharField(max_length=150, verbose_name='Apellido Materno')),
                ('birthday_date', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('disability_type', models.CharField(choices=[('DISCAPACIDAD MOTRIZ', 'DISCAPACIDAD MOTRIZ'), ('DISCAPACIDAD INTELECTUAL', 'DISCAPACIDAD INTELECTUAL'), ('AMBAS DISCAPACIDADES', 'AMBAS DISCAPACIDADES')], max_length=30, verbose_name='Tipo de Discapacidad')),
                ('gender', models.CharField(choices=[('MASCULINO', 'MASCULINO'), ('FEMENINO', 'FEMENINO')], max_length=30, verbose_name='Sexo')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tutor_patients', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]