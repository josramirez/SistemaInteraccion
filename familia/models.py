from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Hijo(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    talla = models.IntegerField(help_text='Talla en cm')
    peso = models.IntegerField(help_text='Ingrese lbs')
    otro = models.TextField(help_text='Cuales son tus intereses')
    fechaNacimiento = models.DateField()

    def __unicode__(self):
        return self.nombre
