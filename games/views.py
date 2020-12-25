from django.shortcuts import render
from django.views import View

class GameView(View):
    """docstring for GameView."""

    def get(self, request, guess):
        x = {'guess': int(guess)}
        return render(request, 'games/play.html', x)
