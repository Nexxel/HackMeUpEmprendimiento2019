#Sergio González Muriel
from django.shortcuts import render
from django.http import HttpResponse

from .forms import SimpleForm

import datetime
import calendar
import locale

import json

# Create your views here.
def health_check(request):
    locale.setlocale(locale.LC_ALL, 'es_ES')
    #locale.setlocale(locale.LC_ALL, 'en_EN')
    now = datetime.datetime.now();
    return HttpResponse("{} de {} de {} {}:{}".format(now.day,calendar.month_name[now.month],now.year,now.hour,now.minute))

def welcome(request):
    if(request.LANGUAGE_CODE == 'es'):
        return HttpResponse("Hola mundo")
    else:
        return HttpResponse("Hello world")

def login(request):
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            return HttpResponse("Form completed")
    else:
        form = SimpleForm()

    return render(request, 'form.html', {'form': form})

def check_login(request):
    response_data = {'status':"error", 'code':401, 'message':"User or password not found"}
    return HttpResponse(json.dumps(response_data), content_type="application/json")