# pdfs/views.py
from django.shortcuts import render
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from products.models import VentaProducto  # Importar el modelo VentaProducto desde la otra app

def generar_pdf(request):
    # Obtener todos los objetos del modelo VentaProducto
    ventas_productos = VentaProducto.objects.all()

    # Configurar la respuesta HTTP con el tipo MIME para PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Lista de Ventas.pdf"'

    # Crear el PDF utilizando ReportLab
    p = canvas.Canvas(response, pagesize=A4)
    y = 800  # Posición vertical inicial
    x = 1
    for venta_producto in ventas_productos:
        p.drawString(100, y, f"Venta {x} : {venta_producto.producto}")
        p.drawString(100, y-20, f"Cantidad: {venta_producto.cantidad}")
        p.drawString(100, y-40, f"Precio: {venta_producto.precio_total}")
        y -= 60  # Espaciado entre objetos
        x += 1

    p.save()
    return response
