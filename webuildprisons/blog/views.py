from django.views.generic import TemplateView, DetailView


class Blog(TemplateView):
    template_name = 'blog/blog.html'

