from django.shortcuts import render
from .models import Room

# Create your views here.

def room(request):

    roomModel = Room.objects.all()

    context = {
        'room' : roomModel
    }

    return render (request, 'room.html', context=context)

def slugModel (request, slug_name):

    slugMod = Room.objects.get(slug_name=slug_name)

    context = {
        'slugMod' : slugMod
    }

    return render (request, 'Slugy.html', context=context)