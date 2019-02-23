from django import forms

from .models import LaderaDefEd

class PostForm(forms.ModelForm):

    class Meta:
        model = LaderaDefEd
        fields = ('termino', 'definicion',)