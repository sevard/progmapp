from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    # ex: /home
    path('', views.about, name='about'),
    # ex: /home/certs
    path('home/certs/', views.certs, name='certs'),
]
