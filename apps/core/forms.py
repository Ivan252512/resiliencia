from django import forms
from .models import Video

class VideosForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ('subtitulo','parrafo', 'descripcion','video', 'imagen')

