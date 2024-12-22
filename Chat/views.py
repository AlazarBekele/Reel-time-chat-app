from django.shortcuts import render

# Create your views here.

def home (request):

    return render (request, 'Home.html')

def chat (request):

    return render (request, 'Chat.html')