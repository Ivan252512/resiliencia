from django import forms

from .models import InundacionesDefRef

class PostForm(forms.ModelForm):
    subtitulo = forms.CharField(help_text='Este campo puede ir vacio.', required=False)
    parrafo = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))

    class Meta:
        model = InundacionesDefRef
        fields = ('subtitulo', 'parrafo',)