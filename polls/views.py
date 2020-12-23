from django.shortcuts import render
from django.views import View


class IndexView(View):
    """docstring fo IndexView."""

    def get(self, request):
        return render(request, 'polls/index.htm')
