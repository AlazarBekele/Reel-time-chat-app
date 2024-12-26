from django.urls import path
from .views import room, slugModel

urlpatterns = [
    path ('', room, name='room'),
    path ('slug/', slugModel, name='slug')
]