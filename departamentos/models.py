from django.db import models


class Departamento(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    nombreCorto = models.CharField('Nombre corto', default=None, max_length=50)
    anulado = models.BooleanField('Anulado', default=False)

    def __str__(self):
        return str(self.id) + ': ' + self.nombre + ' ' + self.nombreCorto
    
