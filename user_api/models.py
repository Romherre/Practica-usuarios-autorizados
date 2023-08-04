from django.db import models
    # esto es una prueba

from django.contrib.auth.models import AbstractUser, Group, Permission


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()


    def __str__(self):
        return self.name
    
