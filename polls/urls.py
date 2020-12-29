from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'polls'
urlpatterns = [
    path('polls/',TemplateView.as_view(template_name='polls/main.html'), name='polls-main'),
    path('polls/index/', views.IndexView.as_view()),
]
