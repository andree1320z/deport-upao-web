from django.db import models


# Create your models here.

class Contacto(models.Model):
    name = models.CharField(max_length=255)
    file = models.ImageField()
    message = models.CharField(max_length=1000)
