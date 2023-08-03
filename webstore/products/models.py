from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre
    
class VentaProducto(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def calcular_precio_total(self):
        self.precio_total = self.producto.precio * self.cantidad

    def __str__(self):
        return self.precio_total