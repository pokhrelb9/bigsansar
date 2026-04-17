from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=60, min_length=5, widget=forms.TextInput(attrs={'class': 'form-control',}))
    username = forms.CharField(max_length=50, validators=[RegexValidator('^[a-z0-9]+$', message='use small Letters and digits with minimum of 3 character')], min_length=3, help_text='use Letters and digits with minimum of 3 character',widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username',  'email',)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Email is Already Exists')
        return email
