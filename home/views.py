from django.shortcuts import render
from .certs import data

def welcome_page(request):
    context = {'title': 'About'}
    return render(request, 'home/welcome.html', context)


def about(request):
    return render(request, 'home/about.html')


def certs(request):
    ctx = {"certificates": data}
    return render(request, 'home/certs.html', ctx)

