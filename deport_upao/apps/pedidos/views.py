from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from pedidos.models import Request


class ListRequests(LoginRequiredMixin, ListView):
    model = Request
    template_name = "pedidos/list_requests.html"


list_requests = ListRequests.as_view()
