from django.db import models
from django.utils import timezone

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return self.nombre
    
class VentaProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    fecha_venta = models.DateTimeField(
            default=timezone.now)

    def calcular_precio_total(self):
        self.precio_total = self.producto.precio * self.cantidad

    def __str__(self):
        return str(self.precio_total) 