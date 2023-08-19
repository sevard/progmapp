from django.urls import path
from . import views


app_name = 'utils'
urlpatterns = [
    # ex: /utils/
    path('', views.index, name='utils-index'),
    path('sha-functions/', views.sha_functions, name='utils-sha-functions'),
]
