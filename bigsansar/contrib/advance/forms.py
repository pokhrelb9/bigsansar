from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, UserCreationForm, UserChangeForm, PasswordChangeForm
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from bigsansar.contrib.advance.models import admin_update
from bigsansar.contrib.account.models import userinfo


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


class profileform(UserChangeForm):
    first_name = forms.CharField(max_length=15, min_length=5, validators=[
        RegexValidator('^[A-Za-z]+$', message='Please enter your correct First name')],
                                 widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', }))
    last_name = forms.CharField(max_length=15, min_length=5, validators=[
        RegexValidator('^[A-Za-z]+$', message='Please enter your correct Last name')],
                                widget=forms.TextInput(attrs={'class': 'form-control', }))
    email = forms.EmailField(max_length=60, min_length=5, help_text='Required. Inform a valid email address.',
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = None

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email',)



class usrinfoform(forms.ModelForm):
    phone = PhoneNumberField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', }))
    address = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', }))

    class Meta:
        model = userinfo
        fields = ('phone', 'address',)



class custom_admin_upadte(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', }))
    url = forms.URLField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', }))

    class Meta:
        model = admin_update
        fields = ('title', 'url',)