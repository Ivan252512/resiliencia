from django import forms

from .models import AsteroidesDefEd, PostEdAsteroides

class PostForm(forms.ModelForm):

    class Meta:
        model = AsteroidesDefEd
        fields = ('termino', 'definicion',)

class PostEdAsteroidesForm(forms.ModelForm):
    imagen = forms.ImageField(help_text='Este campo puede estar vacio', required=False)
    subtitulo = forms.CharField(help_text='Este campo puede estar vacio', required=False)
    parrafo = forms.CharField(help_text='Este campo puede estar vacio', required=False, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    descripcionImagen = forms.CharField(help_text='Este campo puede estar vacio', required=False, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))

    class Meta:
        model = PostEdAsteroides
        fields = ('subtitulo', 'parrafo', 'imagen', 'descripcionImagen')