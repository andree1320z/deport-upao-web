from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'landing/home.html'


# home = cache_page(60 * 60 * 24)(HomeView.as_view())
home = HomeView.as_view()
