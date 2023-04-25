from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .TrendReader import TrendReader
from .APIMockService import APIMockService

# Create your views here.


def panel(request):
    template = loader.get_template("dev/panel.html")
    return HttpResponse(template.render())


def Sprint2Demo(request):
    context = ["20.025", "69", "TQ Campus", "Wish outdoor", "85"]
    return render(request, "demo/Sprint2.html", {"context": context})


def Index(request):
    return render(
        request,
        "dashboard/index.html",
        {
            "events": [
                "Wish Outdoor",
                "Verknipt",
                "Paaspop",
                "Pinkpop",
                "Pukkelpop",
                "Thuishaven",
                "Tomorrowland",
                "Flugel 25 Jaar",
                "LakeDance",
                "Dreamvillage",
                "Malice in Wonderland",
                "Jungle festival",
                "Kletskoek",
                "Defqon.1",
                "Royal dutch",
                "Supersized kingsday",
                "NOX",
            ]
        },
    )


def Event(request, guid):
    return render(request, "dashboard/event.html", {})


def Login(request):
    return render(request, "dashboard/login.html", {})


def Statistics(request):
    return HttpResponse("Bruh")


def Settings(request):
    return HttpResponse("Download RAM")


# populates the dashboard with a list of organizers waiting for their Eventix Wrapped
def GetOrganizers(request):
    return JsonResponse(APIMockService.GetOrganizersWithNoWrap(12))


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
