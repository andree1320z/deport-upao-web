from django.http import HttpResponseServerError
from django.shortcuts import render
from django.views.generic import TemplateView

from core.forms import ContactForm
from core.models import Contacto


class HomeView(TemplateView):
    template_name = 'landing/home.html'


# home = cache_page(60 * 60 * 24)(HomeView.as_view())
home = HomeView.as_view()


def send_contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            file = request.POST.get('file')
            message = request.POST.get('message')
            saving_form = Contacto(name, file, message)
            saving_form.save()
            return HttpResponseServerError

    else:
        form = ContactForm()

    return render(request, 'landing/home.html', {'form': form})
