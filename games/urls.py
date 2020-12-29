from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'games'
urlpatterns = [
    path('games/', TemplateView.as_view(template_name='games/main.html'), name='games-main'),
    path('games/<slug:guess>', views.GameView.as_view())
]
