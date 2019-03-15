from django import forms

from .models import InundacionesDefEd, PostEdInundacion

class PostForm(forms.ModelForm):

    class Meta:
        model = InundacionesDefEd
        fields = ('termino', 'definicion',)

class PostEdInundacionForm(forms.ModelForm):
    imagen = forms.ImageField(help_text='Este campo puede estar vacio', required=False)
    video = forms.FileField(help_text='Este campo puede estar vacio', required=False)
    subtitulo = forms.CharField(help_text='Este campo puede estar vacio', required=False)
    parrafo = forms.CharField(help_text='Este campo puede estar vacio', required=False, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    descripcion = forms.CharField(help_text='Este campo puede estar vacio', required=False, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))

    class Meta:
        model = PostEdInundacion
        fields = ('subtitulo','parrafo', 'youtube', 'descripcion','video', 'imagen')