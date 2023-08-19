from django.shortcuts import render


def index(request):
    return render(request, 'utils/index.html')


def sha_functions(request):
    return render(request, 'utils/sha-functions.html')