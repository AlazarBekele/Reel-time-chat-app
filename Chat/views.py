from django.shortcuts import render, redirect
from form import SignUp
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home (request):

    return render (request, 'Home.html')


def logPage (request):

    return render (request, 'Login.html')



def signup (request):

    form = SignUp(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate (request, username=username, password=password)

            if user is not None:
                login (request, user)
                return redirect ('login')
    
    context = {
        'form' : form
    }

    return render (request, 'Signup.html', context)



def chat (request):

    return render (request, 'Chat.html')