from unicodedata import name
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/base.html')


def index(request):
    return render(request, 'home/index.html')