# Generated by Django 3.2.4 on 2021-07-22 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departamentos', '0002_auto_20210722_1815'),
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Empleado',
            new_name='Empleados',
        ),
    ]