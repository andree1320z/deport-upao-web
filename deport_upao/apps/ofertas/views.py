from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from apps.ofertas.models import Offer


class ListOffers(LoginRequiredMixin, ListView):
    model = Offer
    template_name = "ofertas/list_offers.html"


list_offers = ListOffers.as_view()
