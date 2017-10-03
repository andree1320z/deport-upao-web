from django.db import models

# Create your models here.
from apps.ofertas.models import Offer
from apps.productos.models import Product


class Request(models.Model):
    name = models.CharField(max_length=1000)
    quantity = models.IntegerField()
    offer = models.ForeignKey(Offer, related_name="request_offer")
    product = models.ForeignKey(Product, related_name="request_product")
