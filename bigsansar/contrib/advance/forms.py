from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class loginform(AuthenticationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'autofocus': True,'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class userchform(UserChangeForm):
    password = None
    username = forms.CharField(max_length=50, validators=[
        RegexValidator('^[a-z0-9]+$', message='use Letters and digits with minimum of 3 character')], min_length=3,
                               help_text='use Letters and digits with minimum of 3 character',
                               widget=forms.TextInput(attrs={'autofocus': True,'class': 'form-control'}))

    class Meta:

        model = User
        fields = ['username']


class chpassform(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password',
                                   widget=forms.PasswordInput(attrs={'autofocus': True, 'class': 'form-control'}))
    new_password1 = forms.CharField(label='New Password',
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='New Password confirmation',
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['password1', 'password2']