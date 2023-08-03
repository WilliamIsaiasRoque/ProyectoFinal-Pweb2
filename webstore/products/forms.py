from django import forms
from .models import Producto, VentaProducto

class PostForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion','precio']
        
class VentaProductoForm(forms.ModelForm):
    cantidad = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label="Seleccione un producto")

    class Meta:
        model = VentaProducto
        fields = ['producto', 'cantidad']