from django.views.generic import TemplateView, DetailView


class Video(TemplateView):
    template_name = 'video/video.html'
