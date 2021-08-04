from django.db import models
from django.db.models.enums import Choices

from departamentos.models import Departamento

from ckeditor.fields import RichTextField


class Habilidades(models.Model):
    habilidades = models.CharField('Habilidades', max_length=50)

    class Meta:
        verbose_name = ("Habilidad")
        verbose_name_plural = ("Habilidades del empleado")

    def __str__(self):
        return self.habilidades



class Empleados(models.Model):
    TIPO_TRABAJO = (
        ('0', 'Administrador'),
        ('1', 'Economia'),
        ('2', 'Diseño'),
        ('0', 'CEO'),
    )
    # JOB_CHOICES = (
    #     ('0', 'Contador'),
    #     ('1', 'Adminitrador'),
    #     ('2', 'Economista'),
    #     )
    nombre = models.CharField('Nombre', max_length=50)
    apellido = models.CharField('Apellidos', max_length=100)
    puesto = models.CharField('Puesto', max_length=1, choices=TIPO_TRABAJO)
    #job = models.CharField('Puesto', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    habilidades = models.ManyToManyField(Habilidades)
    cv = RichTextField()

    class Meta:
        verbose_name = ("Empleado")
        verbose_name_plural = ("Empleados")

    def __str__(self):
        return str(self.id) + ': ' + self.nombre + ' ' + self.apellido
