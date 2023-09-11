from django.views.generic import TemplateView

class HomepageTemplateView(TemplateView):
    template_name = 'home.html'