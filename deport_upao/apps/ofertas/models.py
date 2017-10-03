from django.db import models

# Create your models here.
# from productos.models import Product


class Offer(models.Model):
    name = models.CharField(max_length=1000)
    # product = models.ForeignKey(Product, related_name="offer")
    quantity = models.IntegerField()
