from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUp (UserCreationForm):

    first_name = forms.CharField (max_length=30, widget = forms.TextInput (attrs={
        'class' : 'form-control',
        'placeholder' : 'Alazar',
        'autocomplate' : 'off'
    }))
    last_name = forms.CharField (max_length=30, widget= forms.TextInput (attrs={
        'class' : 'form-control',
        'placeholder' : 'Bekele',
        'autocomplate' : 'off'
    }))
    Email = forms.EmailField (max_length=30, widget= forms.EmailInput (attrs={
        'class' : 'form-control',
        'placeholder' : 'example@gmail.com',
        'autocomplate' : 'off'
    }))
    username = forms.CharField (max_length=30, widget= forms.TextInput (attrs={
        'class' : 'form-control',
        'placeholder' : 'alazarbekele11',
        'autocomplate' : 'off'
    }))
    password1 = forms.PasswordInput (max_length=30, widget= forms.PasswordInput (attrs={
        'class' : 'form-control',
        'placeholder' : 'password',
        'autocomplate' : 'off'
    }))
    password2 = forms.PasswordInput (max_length=30, widget= forms.PasswordInput (attrs={
        'class' : 'form-control',
        'placeholder' : 'confirm password',
        'autocomplate' : 'off'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'Email', 'username', 'password1', 'password2')