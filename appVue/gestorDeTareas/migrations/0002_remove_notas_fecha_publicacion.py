# Generated by Django 3.1.3 on 2020-11-22 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestorDeTareas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notas',
            name='fecha_publicacion',
        ),
    ]