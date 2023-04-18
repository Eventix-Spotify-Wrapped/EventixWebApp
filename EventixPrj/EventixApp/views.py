from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Create your views here.


def panel(request):
    template = loader.get_template("dev/panel.html")
    return HttpResponse(template.render())


def Sprint2Demo(request):
    context = ["20.025", "69", "TQ Campus", "Wish outdoor", "85"]
    return render(request, "demo/Sprint2.html", {"context": context})


def Create(request):
    # args: account; creates a wrap for the account; generates cards to choose from based on found trends;

    return JsonResponse(
        {
            "Eventix Wrapped": {
                "Account": "Template",
                "Type": "Yearly",
                "Cards": [
                    {
                        "Status": "Generated",
                        "Context": {"value1": "template", "value2": "template"},
                    },
                    {
                        "Status": "Generated",
                        "Context": {"value1": "template", "value2": "template"},
                    },
                    {
                        "Status": "Generated",
                        "Context": {"value1": "template", "value2": "template"},
                    },
                ],
            }
        }
    )


def Finalize(request):
    # args: tbd. ; finalizes a wrap for an account; returns a finalized and playable Eventix Wrapped;
    return JsonResponse(
        {
            "Eventix Wrapped": {
                "Account": "Template",
                "Type": "Yearly",
                "Cards": [
                    {
                        "Status": "Final",
                        "Context": {"value1": "template", "value2": "template"},
                    },
                    {
                        "Status": "Final",
                        "Context": {"value1": "template", "value2": "template"},
                    },
                ],
            }
        }
    )


# on Create call, an eventix wrapped preview is created with cards based on trends found in ticket sales. said preview is saved in a database
# until it is finalized and sent out
