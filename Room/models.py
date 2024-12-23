from django.db import models

# Create your models here.

class Room (models.Model):

    name = models.CharField (max_length= 300)
    slug_name = models.SlugField (unique=True)