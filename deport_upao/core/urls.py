from django.conf.urls import url

from .views import home, send_contact_form

app_name = "core"

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^enviar-consulta/', send_contact_form, name='send_contact_form'),
]
