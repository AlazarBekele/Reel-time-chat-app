from django.urls import path
from .views import (
    home,
    chat,
    logPage,
    signup
)


urlpatterns = [
    path('', home, name='home'),
    path('chat/', chat, name='chat'),
    path('login/', logPage, name='login'),
    path('signup/', signup, name='signup')
]
