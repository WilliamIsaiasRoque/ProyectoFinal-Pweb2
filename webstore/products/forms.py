from django import forms
from .models import Producto

class PostForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('nombre', 'descripcion','precio',)