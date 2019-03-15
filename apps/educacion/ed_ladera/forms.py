from django import forms

from .models import LaderaDefEd, PostEdLadera

class PostForm(forms.ModelForm):

    class Meta:
        model = LaderaDefEd
        fields = ('termino', 'definicion',)

class PostEdLaderaForm(forms.ModelForm):
    imagen = forms.ImageField(help_text='Este campo puede estar vacio', required=False)
    video = forms.FileField(help_text='Este campo puede estar vacio', required=False)
    subtitulo = forms.CharField(help_text='Este campo puede estar vacio', required=False)
    parrafo = forms.CharField(help_text='Este campo puede estar vacio', required=False, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    descripcion = forms.CharField(help_text='Este campo puede estar vacio', required=False, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))

    class Meta:
        model = PostEdLadera
        fields = ('subtitulo','parrafo', 'youtube', 'descripcion','video', 'imagen')