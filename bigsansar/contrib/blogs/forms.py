
from django import forms

from bigsansar.contrib.blogs.models import post

class customblogform(forms.ModelForm):
    class Meta:
        model = post
        fields = '__all__'
        exclude = ('visitor',)
        #widgets = {'visitor': forms.HiddenInput()}