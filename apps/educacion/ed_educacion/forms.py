from django import forms

from .models import Principal, Glosario, Referencia

class PrincipalForm(forms.ModelForm):
    imagen = forms.ImageField(help_text='Este campo puede estar vacio', required=False)
    video = forms.FileField(help_text='Este campo puede estar vacio', required=False)
    subtitulo = forms.CharField(help_text='Este campo puede estar vacio', required=False)
    parrafo = forms.CharField(help_text='Este campo puede estar vacio', required=False, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    descripcion = forms.CharField(help_text='Este campo puede estar vacio', required=False, widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))

    class Meta:
        model = Principal
        fields = ('subtitulo', 'parrafo', 'imagen',  'video', 'descripcion')


class GlosarioForm(forms.ModelForm):

    class Meta:
        model = Glosario
        fields = ('termino', 'definicion',)


class ReferenciaForm(forms.ModelForm):

    class Meta:
        model = Referencia
        fields = ('referencia',)