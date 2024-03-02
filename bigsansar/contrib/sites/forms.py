import os
from typing import Any, Dict

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from bigsansar.contrib.sites.models import domains, pages
from www.settings import BASE_DIR



class customaddpageform(forms.ModelForm):
    class Meta:
        model = pages
        fields = '__all__'
        exclude = ('body',)
        widgets = {'slug': forms.HiddenInput(), 'visitor': forms.HiddenInput()}

    def clean(self):
        getdir = 'templates'
        gethost = self.cleaned_data.get('domain')

        if gethost is None:
            raise ValidationError(message='This field is required.')

        if pages.objects.filter(slug=self.cleaned_data.get('slug'), domain=self.cleaned_data.get('domain')):
            raise ValidationError(
                _('page with url %(url)s already exists for domain %(site)s'),
                code='duplicate_url',
                params={'url': self.cleaned_data.get('slug'), 'site': self.cleaned_data.get('domain')}, )

        mkdir = getdir + '/' + str(domains.objects.get(domain=gethost).domain)
        try:
            final_directory = os.path.join(BASE_DIR, mkdir)
            if not os.path.exists(final_directory):
                os.makedirs(final_directory)
        except:
            raise ValidationError(
                _(final_directory + ' Directory not created "Permission Denied"'),
            )

        return super().clean()


class custompageform(forms.ModelForm):
    class Meta:
        model = pages
        fields = '__all__'
        widgets = {'visitor': forms.HiddenInput(),
                   'body': forms.Textarea(attrs={'cols': 100, 'rows': 25})}

    def clean(self):
        file = self.cleaned_data.get('slug')
        get_content = self.cleaned_data.get('body')
        gethost = self.cleaned_data.get('domain')
        getdir = 'templates'

        if gethost is None:
            raise ValidationError(message='This field is required.')

        if get_content is None:
            raise ValidationError(message='This field is required.')

        if file is None:
            raise ValidationError(message='This field is required.')

        mkdir = getdir + '/' + str(domains.objects.get(domain=gethost).domain)
        full_path = os.path.join(BASE_DIR, mkdir)
        createfile = full_path + '/' + file + '.html'
        f = open(createfile, "w", encoding="utf-8")
        f.write(get_content)
        f.close()
        return super().clean()
    


class create_domainform(forms.ModelForm):
    domain = forms.CharField(max_length=100, min_length=3, validators=[
        RegexValidator('^[a-z0-9.]+\.[a-z0-9]{1,5}$', message='Please enter your correct domain name')],
                             widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', }))
    
    Description = forms.CharField(max_length=15, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': False}))

    class Meta:
        model = domains
        fields = ('domain', 'Description',)


class customviewspageform(forms.ModelForm):
    title = forms.CharField(max_length=50, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': True}))

    class Meta:
        model = pages
        fields = ('title',)



class customviewseditpage(forms.ModelForm):
    title = forms.CharField(max_length=50, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': True}))

    class Meta:
        model = pages
        fields = ('title', 'body',)
        widgets = {'body': forms.Textarea(attrs={'class': 'form-control', 'cols': 90, 'rows': 20})}

        





class edit_domainform(forms.ModelForm):
    domain = forms.CharField(max_length=100, min_length=3, validators=[
        RegexValidator('^[a-z0-9.]+\.[a-z0-9]{1,5}$', message='Please enter your correct domain name')],
                             widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', }))
    
    Description = forms.CharField(max_length=15, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': False}))

    class Meta:
        model = domains
        fields = ('domain', 'Description', 'primary_domaIn',)
