from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    imagen = models.ImageField(upload_to='productos')

    def __str__(self):
        return self.nombre
    
class VentaProducto(models.Model):
    comprador = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fecha_venta = models.DateTimeField(default=timezone.now)

    def calcular_precio_total(self):
        self.precio_total = self.producto.precio * self.cantidad

    def __str__(self):
        return str(self.precio_total) 