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
    context = ["20.025", "69", "Netherlands", "Wish outdoor", "85"]
    return render(request, "demo/Sprint2.html", {"context": context})


@csrf_exempt
def receiveJSON(request):
    return HttpResponse(request.POST)
