import os
import json
import requests
from django.shortcuts import render
from django.shortcuts import render
from dotenv import load_dotenv


load_dotenv()

# def index(request):
#     return render(request, 'webtools/index.html')


def sha_functions(request):
    return render(request, 'webtools/sha_functions.html')


def iplookup(request):
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    IP_LOOKUP_URL = os.getenv('IP_LOOKUP_REQUEST_URL')
    IP = request.headers.get('X-Real-Ip')
    # IP = request.META.get('REMOTE_ADDR')

    # When on runnig local
    if not IP:
        IP = os.getenv("LOCAL_IP")

    url = f"{IP_LOOKUP_URL}/{IP}?access_key={ACCESS_KEY}"
    response = requests.get(url)
    context = json.loads(response.content)
    return render(request, 'webtools/iplookup.html', {'ctx': context})
