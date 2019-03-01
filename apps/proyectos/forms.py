from django import forms

from .models import PostProyecto

class PostForm(forms.ModelForm):
    imagen = forms.ImageField(help_text='Este campo puede estar vacio', required=False)
    subtitulo = forms.CharField(help_text='Este campo puede estar vacio', required=False)
    parrafo = forms.CharField(help_text='Este campo puede estar vacio', required=False, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    descripcionImagen = forms.CharField(help_text='Este campo puede estar vacio', required=False, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))

    class Meta:
        model = PostProyecto
        fields = ('subtitulo', 'parrafo', 'imagen', 'descripcionImagen')