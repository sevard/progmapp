from django.shortcuts import render
from django.views import View


class GamesView(View):
    """docstring for GameView."""

    def get(self, request):
        return render(request, 'games/index.html')


class GuessView(View):
    """Description here"""

    def get(self, request):
        return render(request, 'games/guess.html')


class GuessPlayView(View):
    """docstring for GuessView."""

    def get(self, request, guess):

        try:
            x = {'guess': int(guess)}
        except:
            return render(request, 'games/error.html')

        return render(request, 'games/play.html', x)
