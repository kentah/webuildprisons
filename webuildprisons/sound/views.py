from django.views.generic import TemplateView, DetailView


class Sound(TemplateView):
    template_name = 'sound/sound.html'
