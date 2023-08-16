from django.shortcuts import render


def home(request):
    return render(request, 'home/home.html')


def about(request):
    context = {'title': 'About'}
    return render(request, 'home/about.html', context)
