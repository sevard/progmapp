from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from dotenv import load_dotenv
import requests
import json
import os


load_dotenv()

def index(request):
    return render(request, 'webtools/index.html')


def sha_functions(request):
    return render(request, 'webtools/sha-functions.html')


def iplookup(request):
    DEBUG = os.getenv('PROGMAPP_SETTINGS_DEBUG')
    ACCESS_KEY = os.getenv('ACCESS_KEY')
    IP_LOOKUP_URL = os.getenv('IP_LOOKUP_REQUEST_URL')

    IP = request.headers.get('X-Real-Ip')
    # ip = request.META.get('REMOTE_ADDR')

    # When on runnig local
    if (DEBUG == '1'):
        IP = '8.8.8.8'

    request_url = f"{IP_LOOKUP_URL}/{IP}?access_key={ACCESS_KEY}"
    resp = requests.get(request_url)
    ctx = json.loads(resp.content)

    response = render(request, 'webtools/iplookup.html', {'ctx': ctx})
    return response
