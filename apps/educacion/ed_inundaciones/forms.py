from django import forms

from .models import InundacionesDefEd

class PostForm(forms.ModelForm):

    class Meta:
        model = InundacionesDefEd
        fields = ('termino', 'definicion',)