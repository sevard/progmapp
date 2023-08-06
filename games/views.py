from django.shortcuts import render
from django.views import View


class GameView(View):
    """docstring for GameView."""

    def get(self, request, guess):
        try:
            x = {'guess': int(guess)}
        except:
            return render(request, 'games/error.html')

        return render(request, 'games/play.html', x)
