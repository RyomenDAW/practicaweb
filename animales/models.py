from django.db import models
from django.utils import timezone  # Para obtener la fecha actual
from django.conf import settings

#Como crear un modelo animal

class Animal (models.Model):
    cuidador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Protectora(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=100)
    fechacreacion = models.DateTimeField(default=timezone.now)
    
class Colaborador(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    fechacreacion = models.DateTimeField(default=timezone.now)