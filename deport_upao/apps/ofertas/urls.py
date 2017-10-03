from django.conf.urls import url

from .views import list_offers

app_name = "ofertas"

urlpatterns = [
    url(r'list-ofertas/$', list_offers, name='list_offers'),
]
