from django.urls import path
from . import views
# from django.views.generic import TemplateView


app_name = 'home'
urlpatterns = [
    # ex: /home
    path('', views.index, name='home-index'),
]
