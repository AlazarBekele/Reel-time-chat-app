from django.urls import path
from .views import (
    home,
    chat,
    logPage,
    signup
)


urlpatterns = [
    path('home/', home, name='home'),
    path('login/', logPage, name='login'),
    path('signup/', signup, name='signup')
]
