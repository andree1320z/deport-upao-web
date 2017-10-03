"""deport_upao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    # Core URLs
    url(r'^', include('core.urls', namespace='core')),

    # App URLs
    url(r'^productos/', include('apps.productos.urls', namespace='productos')),
    url(r'^ofertas/', include('apps.ofertas.urls', namespace='ofertas')),
    url(r'^cotizaciones/', include('apps.cotizaciones.urls', namespace='cotizaciones')),

    # Admin
    url(r'^admin/', admin.site.urls),

    # Accounts URLs
    # https://github.com/fusionbox/django-authtools/blob/master/authtools/urls.py
    url(r'^', include('extensions.authtools.urls')),

    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'images/favicon.ico', permanent=True),
        name='favicon.ico'),
]

if settings.DEBUG:
    urlpatterns += [
        # Testing 404 and 500 error pages
        url(r'^404/$', TemplateView.as_view(template_name='404.html'), name='404'),
        url(r'^500/$', TemplateView.as_view(template_name='500.html'), name='500'),
    ]

    try:
        from django.conf.urls.static import static

        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

        import debug_toolbar

        urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]

    # Should only occur when debug mode is on for production testing
    except ImportError as e:
        import logging

        l = logging.getLogger(__name__)
        l.warning(e)
