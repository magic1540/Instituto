# Generated by Django 3.1.1 on 2020-10-13 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id_alumno', models.AutoField(db_column='id_alumno', primary_key=True, serialize=False)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('rut', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(blank=True, max_length=20, null=True)),
                ('apellido_paterno', models.CharField(blank=True, max_length=20, null=True)),
                ('apellido_materno', models.CharField(blank=True, max_length=20, null=True)),
                ('genero', models.CharField(blank=True, max_length=10, null=True)),
                ('activo', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]