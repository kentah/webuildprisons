from django.shortcuts import render
from django.views.generic import TemplateView, DetailView


class Image(TemplateView):
    template_name = 'image/image.html'

class ImageDetail(DetailView):
    pass

