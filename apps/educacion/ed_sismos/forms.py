from django import forms

from .models import SismoDefEd, PostEdSismo

class PostForm(forms.ModelForm):

    class Meta:
        model = SismoDefEd
        fields = ('termino', 'definicion',)

class PostEdSismoForm(forms.ModelForm):
    imagen = forms.ImageField(help_text='Este campo puede estar vacio', required=False)
    video = forms.FileField(help_text='Este campo puede estar vacio', required=False)
    subtitulo = forms.CharField(help_text='Este campo puede estar vacio', required=False)
    parrafo = forms.CharField(help_text='Este campo puede estar vacio', required=False, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    descripcion = forms.CharField(help_text='Este campo puede estar vacio', required=False, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))

    class Meta:
        model = PostEdSismo
        fields = ('subtitulo', 'parrafo', 'imagen',  'video', 'descripcion')