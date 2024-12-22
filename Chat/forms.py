from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUp (UserCreationForm):

    first_name = forms.CharField (max_length=30, widget = forms.TextInput (attrs={
        'class' : 'form-control ps-5 pe-5',
        'placeholder' : 'Alazar',
        'autocomplate' : 'off'
    }))
    last_name = forms.CharField (max_length=30, widget= forms.TextInput (attrs={
        'class' : 'form-control ps-5 pe-5',
        'placeholder' : 'Bekele',
        'autocomplate' : 'off'
    }))
    Email = forms.EmailField (max_length=30, widget= forms.EmailInput (attrs={
        'class' : 'form-control ps-5 pe-5',
        'placeholder' : 'example@gmail.com',
        'autocomplate' : 'off'
    }))
    username = forms.CharField (max_length=30, widget= forms.TextInput (attrs={
        'class' : 'form-control ps-5 pe-5',
        'placeholder' : 'alazarbekele11',
        'autocomplate' : 'off'
    }))
    password1 = forms.CharField (max_length=30, label='password Confirm' ,widget= forms.PasswordInput (attrs={
        'class' : 'form-control ps-5 pe-5',
        'placeholder' : 'password',
        'autocomplate' : 'off'
    }))
    password2 = forms.CharField (max_length=30, label='password Confirm' ,widget= forms.PasswordInput (attrs={
        'class' : 'form-control ps-5 pe-5',
        'placeholder' : 'confirm password',
        'autocomplate' : 'off'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'Email', 'username', 'password1', 'password2')