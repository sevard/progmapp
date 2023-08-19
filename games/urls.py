from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'games'
urlpatterns = [
    path('', views.GamesView.as_view(), name='games-index'),
    path('guess/', views.GuessView.as_view(), name='guess-page'),
    path('guess/<slug:guess>/', views.GuessPlayView.as_view()),
]
