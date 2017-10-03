from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from productos.models import Product


class ListProducts(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/list_products.html'


list_products = ListProducts.as_view()
