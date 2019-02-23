from django import forms

from .models import AsteroidesDefEd

class PostForm(forms.ModelForm):

    class Meta:
        model = AsteroidesDefEd
        fields = ('termino', 'definicion',)