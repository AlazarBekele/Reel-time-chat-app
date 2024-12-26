from django.shortcuts import render
from .models import Room

# Create your views here.

def room (request, slug):

    roomModel = Room.objects.all()
    slugMod = Room.objects.get(slug=slug)

    context = {
        'room' : roomModel,
        'slugMod' : slugMod
    }

    return render (request, 'room.html', context=context)