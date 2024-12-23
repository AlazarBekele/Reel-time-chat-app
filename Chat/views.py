from django.shortcuts import render, redirect
from .forms import SignUp, LoginCheck
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home (request):

    return render (request, 'Home.html')


def logPage (request):

    log = LoginCheck(request.POST or None)

    if request.method == 'POST':
        if log.is_valid():

            username = log.cleaned_data.get('username')
            password = log.cleaned_data.get('password')

            user = authenticate (request, username=username, password=password)

            if user is not None:
                login (request, user)
                return redirect ('login')
    
    context = {
        'log' : log
    }

    return render (request, 'Login.html', context)



def signup (request):

    signin = SignUp(request.POST or None)

    if request.method == 'POST':
        if signin.is_valid():

            signin.save()
            return redirect ('login')
        
    context = {
        'signin' : signin
    }

    return render (request, 'Signup.html', context)



def chat (request):

    return render (request, 'Chat.html')