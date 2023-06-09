# Generated by Django 4.2 on 2023-05-20 20:58

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('paternal_surname', models.CharField(max_length=150, verbose_name='Apellido Paterno')),
                ('maternal_surname', models.CharField(max_length=150, verbose_name='Apellido Materno')),
                ('birthday_date', models.DateField(verbose_name='Fecha de Nacimiento')),
                ('gender', models.CharField(choices=[('MASCULINO', 'MASCULINO'), ('FEMENINO', 'FEMENINO')], max_length=30, verbose_name='Sexo')),
                ('relationship', models.CharField(choices=[('PAPÁ', 'PAPÁ'), ('MAMÁ', 'MAMÁ'), ('OTRO', 'OTRO')], max_length=30, verbose_name='Parentesco')),
                ('street', models.CharField(max_length=100, verbose_name='Calle')),
                ('street_number', models.CharField(max_length=15, verbose_name='Numero')),
                ('neighborhood', models.CharField(max_length=100, verbose_name='Colonia')),
                ('zip', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator('^\\d{5}$', 'SOLO SE PERMITEN NUMEROS')], verbose_name='Codigo Postal')),
                ('city', models.CharField(max_length=100, verbose_name='Municipio')),
                ('state', models.CharField(max_length=100, verbose_name='Estado')),
                ('telephone', models.CharField(max_length=13, unique=True, verbose_name='Telefono')),
            ],
            options={
                'verbose_name': 'Tutor',
                'verbose_name_plural': 'Tutores',
                'ordering': ['name'],
            },
        ),
    ]
