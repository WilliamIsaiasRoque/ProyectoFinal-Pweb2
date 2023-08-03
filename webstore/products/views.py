from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from .models import Producto

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
        return redirect('productos_list')
    return render(request, 'productos_delete.html', {'prods': prods})