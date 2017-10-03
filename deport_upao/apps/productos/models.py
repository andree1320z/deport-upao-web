from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    unidad = models.FloatField(max_length=1000)
