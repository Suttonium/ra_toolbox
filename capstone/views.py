from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class Forbidden403(TemplateView):
    template_name = '403.html'
