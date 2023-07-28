from django import forms
from .models import Productos

class PostForm(forms.ModelForm):

    class Meta:
        model = Productos
        fields = ('nombre', 'descripcion','precio',)