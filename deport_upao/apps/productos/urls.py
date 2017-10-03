from django.conf.urls import url

from .views import list_products

app_name = "producto"

urlpatterns = [
    url(r'list-productos/$', list_products, name='list_products'),
]
