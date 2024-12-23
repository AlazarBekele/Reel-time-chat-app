from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUp (UserCreationForm):

    first_name = forms.CharField (max_length=30, widget = forms.TextInput (attrs={
        'class' : 'form-control ps-2',
        'placeholder' : 'Last Name',
        'autocomplate' : 'off'
    }))
    last_name = forms.CharField (max_length=30, widget= forms.TextInput (attrs={
        'class' : 'form-control ps-2 sizeWidth',
        'placeholder' : 'Last Name',
        'autocomplate' : 'off'
    }))
    Email = forms.EmailField (max_length=30, widget= forms.EmailInput (attrs={
        'class' : 'form-control ps-2',
        'placeholder' : 'example@gmail.com',
        'autocomplate' : 'off'
    }))
    username = forms.CharField (max_length=30, widget= forms.TextInput (attrs={
        'class' : 'form-control ps-2 sizeWidth',
        'placeholder' : 'alazarbekele11',
        'autocomplate' : 'off'
    }))
    password1 = forms.CharField (max_length=30, label='password Confirm' ,widget= forms.PasswordInput (attrs={
        'class' : 'form-control ps-2 sizeWidth',
        'placeholder' : 'password',
        'autocomplate' : 'off'
    }))
    password2 = forms.CharField (max_length=30, label='password Confirm' ,widget= forms.PasswordInput (attrs={
        'class' : 'form-control ps-2 sizeWidth',
        'placeholder' : 'confirm password',
        'autocomplate' : 'off'
    }))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'Email', 'username', 'password1', 'password2')


class LoginCheck (forms.Form):

    username = forms.CharField (widget= forms.TextInput (attrs={

        'class' : 'form-control',
        'placeholder' : 'Username or password',
        'type' : 'text'

    }))

    password = forms.CharField (widget= forms.PasswordInput (attrs= {

        'class' : 'form-control',
        'placeholder' : 'password',
        'type' : 'password'
        
    }))