from django import forms
from django.contrib.auth.models import User
from .models import Producto, VentaProducto

class PostForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].label = 'Nombre del producto'
        self.fields['descripcion'].label = 'Descripción del producto'
        self.fields['precio'].label = 'Precio del producto'
        self.fields['imagen'].label = 'Imagen del producto'
        
class VentaProductoForm(forms.ModelForm):
    comprador = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label="Seleccione un comprador")
    cantidad = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    producto = forms.ModelChoiceField(queryset=Producto.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), empty_label="Seleccione un producto")

    class Meta:
        model = VentaProducto
        fields = ['producto', 'cantidad', 'comprador']
        widgets = {
            'comprador': forms.Select(attrs={'class': 'form-control'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control'}),
            'producto': forms.Select(attrs={'class': 'form-control'}),
        }