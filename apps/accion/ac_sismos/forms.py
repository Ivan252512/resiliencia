from django import forms

from .models import SismoDefAc, PostAcSismo

class PostForm(forms.ModelForm):
    subtitulo = forms.CharField(help_text='Este campo puede ir vacio.', required=False)
    parrafo = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))

    class Meta:
        model = SismoDefAc
        fields = ('subtitulo', 'parrafo',)

class PostAcSismoForm(forms.ModelForm):
    imagen = forms.ImageField(help_text='Este campo puede estar vacio', required=False)
    video = forms.FileField(help_text='Este campo puede estar vacio', required=False)
    subtitulo = forms.CharField(help_text='Este campo puede estar vacio', required=False)
    parrafo = forms.CharField(help_text='Este campo puede estar vacio', required=False, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    descripcion = forms.CharField(help_text='Este campo puede estar vacio', required=False, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))

    class Meta:
        model = PostAcSismo
        fields = ('subtitulo', 'parrafo', 'imagen',  'video', 'descripcion')