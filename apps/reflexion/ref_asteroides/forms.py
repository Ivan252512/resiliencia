from django import forms

from .models import AsteroidesDefRef, PostRefAsteroide

class PostForm(forms.ModelForm):
    subtitulo = forms.CharField(help_text='Este campo puede ir vacio.', required=False)
    parrafo = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))

    class Meta:
        model = AsteroidesDefRef
        fields = ('subtitulo', 'parrafo',)

class PostRefAsteroideForm(forms.ModelForm):
    imagen = forms.ImageField(help_text='Este campo puede estar vacio', required=False)
    subtitulo = forms.CharField(help_text='Este campo puede estar vacio', required=False)
    parrafo = forms.CharField(help_text='Este campo puede estar vacio', required=False, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    descripcionImagen = forms.CharField(help_text='Este campo puede estar vacio', required=False, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))

    class Meta:
        model = PostRefAsteroide
        fields = ('subtitulo', 'parrafo', 'imagen', 'descripcionImagen')