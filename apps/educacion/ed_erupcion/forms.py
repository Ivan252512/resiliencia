from django import forms

from .models import VolcanDefEd

class PostForm(forms.ModelForm):

    class Meta:
        model = VolcanDefEd
        fields = ('termino', 'definicion',)