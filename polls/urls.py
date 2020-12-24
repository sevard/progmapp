from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('polls/',TemplateView.as_view(template_name='polls/main.html')),
    path('polls/index/', views.IndexView.as_view()),
]
