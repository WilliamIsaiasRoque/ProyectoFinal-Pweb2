from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, VentaProductoForm
from django.shortcuts import redirect
from .models import Producto, VentaProducto

def pag_main(request):
    return render(request, 'inicio.html')

def prod_list(request):
    prods = Producto.objects.all().order_by('nombre')
    return render(request, 'productos_list.html', {'prods': prods})

def prod_detail(request, pk):
    prods = get_object_or_404(Producto, pk=pk)
    return render(request, 'productos_detail.html', {'prods': prods})

def prod_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            prods = form.save(commit=False)
            prods.save()
            return redirect('prod_detail', pk=prods.pk)
    else:
        form = PostForm()
    return render(request, 'productos_edit.html', {'form': form})

def prod_edit(request, pk):
    prods = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=prods)
        if form.is_valid():
            prods = form.save(commit=False)
            prods.save()
            return redirect('prod_detail', pk=prods.pk)
    else:
        form = PostForm(instance=prods)
    return render(request, 'productos_edit.html', {'form': form})

def prod_delete(request, pk):
    prods = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        prods.delete()
        return redirect('prod_list')
    return render(request, 'productos_delete.html', {'prods': prods})

def sell_list(request):
    sells = Producto.objects.all()
    return render(request, 'ventas_list.html', {'sells': sells})

def sell_new(request):
    if request.method == "POST":
        form = VentaProductoForm(request.POST)
        if form.is_valid():
            venta_producto = form.save(commit=False)
            venta_producto.calcular_precio_total()  # Calcular el precio total
            venta_producto.save()
            return redirect('sell_detail', pk=venta_producto.pk)
    else:
        form = VentaProductoForm()
    return render(request, 'ventas_edit.html', {'form': form})

def sell_detail(request, pk):
    sells = get_object_or_404(VentaProducto, pk=pk)
    return render(request, 'ventas_detail.html', {'sells': sells})