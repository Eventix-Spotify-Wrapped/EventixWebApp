from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def panel(request):
    template = loader.get_template("dev/panel.html")
    return HttpResponse(template.render())


def Sprint2Demo(request):
    cards = [{"Title": "Title", "Text": "This some text boie"}]
    return render(request, "demo/Sprint2.html", {"cards": cards})


@csrf_exempt
def receiveJSON(request):
    return HttpResponse(request.POST)
