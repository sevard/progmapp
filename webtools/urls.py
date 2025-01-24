from django.urls import path
from . import views


app_name = 'webtools'
urlpatterns = [
    # keep for now
    # ex: /webtools/
    # path('', views.index, name='webtools'),

    # ex: /webtools/sha-functions/
    path('sha-functions/', views.sha_functions, name='webtools-sha-functions'),
    # ex: /webtools/iplookup/
    path('iplookup/', views.iplookup, name='webtools-iplookup'),
]
