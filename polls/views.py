from django.shortcuts import get_object_or_404, render
from django.views import View, generic
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from .models import Choice, Question


class WelcomeView(View):
    """docstring fo IndexView."""

    def get(self, request):
        return render(request, 'polls/welcome.html')

######################################################################
# Modified QuestionListView to have it as generic view.
# Code below eplains how generic view works.
#
# class QuestionListView(View):
#
#    model = Question
#
#    def get(self, request):
#        modelname = self.model._meta.verbose_name.title().lower()
#        stuff = self.model.objects.all()
#        cntx = {modelname+'_list': stuff}
#        return render(request, 'polls/'+modelname+'_list.html', cntx)
######################################################################
class QuestionListView(generic.ListView):
    model = Question

"""
# Modified code below to have render() instead of
# template = loader.get_template('polls/index.html')
# return HttpResponse(template.render(context, request))
"""
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

# TODO : Try to have this code in QuestionListView class
def detail(request, question_id):
    '''
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
        '''
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You did not select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:polls-results', args=(question.id,) ))
