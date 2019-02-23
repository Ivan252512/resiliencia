from django import forms

from .models import SismoDefEd

class PostForm(forms.ModelForm):

    class Meta:
        model = SismoDefEd
        fields = ('termino', 'definicion',)