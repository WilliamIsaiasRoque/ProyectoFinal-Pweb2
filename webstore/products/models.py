from django.db import models

class Productos(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.CharField(max_length=100)
