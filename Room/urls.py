from django.urls import path
from .views import room, slugModel

urlpatterns = [
    path ('chat/', room, name='chat'),
    path ('<slug:slug>', slugModel, name='slug_name')
]