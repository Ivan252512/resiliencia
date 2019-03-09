from django import forms
from .models import Video

class VideosForm(forms.ModelForm):
    parrafo = forms.CharField(help_text='Este campo puede estar vacio', required=False, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    descripcion = forms.CharField(help_text='Este campo puede estar vacio', required=False, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    class Meta:
        model = Video
        fields = ('subtitulo','parrafo', 'descripcion','video', 'imagen')

