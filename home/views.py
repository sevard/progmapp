from django.shortcuts import render


def welcome_page(request):
    context = {'title': 'About'}
    return render(request, 'home/welcome.html', context)


def about(request):
    return render(request, 'home/about.html')


def certs(request):
    return render(request, 'home/certs.html')

