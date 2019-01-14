from django.urls import path


from . import views

urlpatterns = [
    path('', views.Sound.as_view(), name='sound'),
]