from django.urls import path
from . import views

urlpatterns = [
    path('polls/', views.IndexView.as_view())
]
