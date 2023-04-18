from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .TrendReader import TrendReader

# Create your views here.


def panel(request):
    template = loader.get_template("dev/panel.html")
    return HttpResponse(template.render())


def Sprint2Demo(request):
    context = ["20.025", "69", "TQ Campus", "Wish outdoor", "85"]
    return render(request, "demo/Sprint2.html", {"context": context})


def Create(request):
    # args: account; creates a wrap for the account; generates cards to choose from based on found trends;
    TrendReader.AnalyzeTrends(request.GET.get("account"))
    return JsonResponse(
        {
            "Eventix Wrapped": {
                "Account": "Template",
                "Type": "Yearly",
                "Cards": [
                    {
                        "Status": "Generated",
                        "Trend": "Sell-out timeframe",
                        "Context": ["Paaspop", "13 minutes"],
                    },
                    {
                        "Status": "Generated",
                        "Trend": "Country insight",
                        "Context": ["D.O.T.", "Netherlands", "87", "Germany", "45"],
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
                        "Trend": "Sell-out timeframe",
                        "Context": ["Paaspop", "13 minutes"],
                    },
                    {
                        "Status": "Final",
                        "Trend": "Country insight",
                        "Context": ["D.O.T.", "Netherlands", "87", "Germany", "45"],
                    },
                ],
            }
        }
    )


# on Create call, an eventix wrapped preview is created with cards based on trends found in ticket sales. said preview is saved in a database
# until it is finalized and sent out
