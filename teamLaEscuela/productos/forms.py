from django import forms

from .models import Juegos


class juegosForm(forms.ModelForm):

    class Meta:
        model = Juegos
        fields = ['nombre', 'descripcion','categoria','desarrolladora','fecha_de_lanzamiento','precio','imagenSmall','imagenBig']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control'}),
            'categoria': forms.TextInput(attrs={'class':'form-control'}),
            'desarrolladora': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_de_lanzamiento': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels = {
            'Nombre':'', 'Descripcion':'','Categoria': '','Desarrolladora':'','Fecha de lanzamiento':'','Precio':'','Imagen': '','Imagen Grande':''
        }
