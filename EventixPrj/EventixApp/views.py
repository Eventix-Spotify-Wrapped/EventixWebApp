from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import DataManager
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def panel(request):
    template = loader.get_template("dev/panel.html")
    return HttpResponse(template.render())


@csrf_exempt
def receiveJSON(request):
    return HttpResponse(request.POST)
