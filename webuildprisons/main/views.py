from django.shortcuts import render
from django.views.generic import TemplateView, DetailView


class Main(TemplateView):
    template_name = 'main/main.html'

class MainDetail(DetailView):
    pass

