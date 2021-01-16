from django.urls import path
from . import views
from django.views.generic import TemplateView


app_name = 'polls'
urlpatterns = [
    # ex: /polls/welcome/
    path('welcome/', views.WelcomeView.as_view(), name='polls-welcome'),
    # ex: /polls/main/
    path('main',TemplateView.as_view(template_name='polls/main.html'), name='polls-main'),
    # ex: /polls/questions/
    path('questions/', views.QuestionListView.as_view(), name='questions-list'),
    # ex: /polls/
    path('', views.index, name='polls-index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='polls-detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='polls-results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='polls-vote'),
]
