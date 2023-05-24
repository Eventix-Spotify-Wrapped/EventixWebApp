from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .TrendReader import TrendReader
from .APIMockService import APIMockService
from .CSV_Reader import CSV_Reader
from django.contrib.auth import authenticate, logout, login
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.models import User
from .mock_maker_3000 import MockMaker
from EventixApp.models import Wrap
import pdb
import random
from .StatsCalculate import get_events_name_list, get_events_name_guid_keypair
# Create your views here.


def panel(request):
    template = loader.get_template("dev/panel.html")
    return HttpResponse(template.render())


def Summary(request):
    context = ["20.025", "69", "TQ Campus", "Wish outdoor", "85"]
    return render(request, "summary.html", {"context": context})


def Index(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    total_events_nameguid_keypair = get_events_name_guid_keypair()
    completed_wraps = Wrap.objects.values_list('owner_account_id', flat=True)
    data = []
    for ng_kp in total_events_nameguid_keypair:
        alreadyAdded = False
        for dat in data:
            if (dat["Guid"] == ng_kp["Guid"]):
                alreadyAdded = True
        if (not alreadyAdded):
            for owner in completed_wraps:
                if (owner in ng_kp["Guid"]):
                    data.append(
                        {"Event": ng_kp["Name"], "Wrapped": True, "Guid": ng_kp["Guid"]})
                    alreadyAdded = True
            if (not alreadyAdded):
                data.insert(
                    0, {"Event": ng_kp["Name"], "Wrapped": False, "Guid": ng_kp["Guid"]})

    return render(
        request,
        "dashboard/index.html",
        {
            "events":
                data,
        },
    )


def Event(request, event_name, guid):
    cards = [
        "summary-slides/begin-slide.html",
        "summary-slides/ticket-amount.html",
        "summary-slides/origin-slide.html",
        "summary-slides/ticket-percentage.html",
        "summary-slides/find-the-truth.html",
        "summary-slides/animated-ticket-amount.html"
    ]
    name = event_name
    data = []
    completed_wraps = Wrap.objects.values_list('owner_account_id', flat=True)
    preselected_cards = []
    overwrite = False
    for owner in completed_wraps:
        if (owner in guid):
            preselected_cards = Wrap.objects.all().values(
                "cards").get(owner_account_id=guid)["cards"]
    if (len(preselected_cards) > 0):
        overwrite = True
    for _ in range(4):
        if (len(preselected_cards) > 0):
            data.append(
                {"Name": preselected_cards[0], "Toggled": True})
            for card in cards:
                if (card in preselected_cards[0]):
                    cards.remove(card)
            preselected_cards.pop(0)
            continue
        index = random.randrange(len(cards))
        data.append({"Name": cards[index], "Toggled": False})
        cards.pop(index)
  #  raise MyException('msg here')

    return render(request, "dashboard/event.html", {"Name": name, "Guid": guid, "Overwrite": overwrite, "Cards": data})


class MyException(Exception):
    pass


def SaveWrap(request):
    cards = request.GET.getlist("cards")
    owner = request.GET.get("owner")
    if (not Wrap.objects.filter(owner_account_id=owner).exists()):
        wrap = Wrap(
            owner_account_id=owner,
            cards=cards
        )
        wrap.save()
    else:
        wrap = Wrap.objects.get(owner_account_id=owner)
        wrap.cards = cards
        wrap.save()

    return HttpResponse(print(wrap))


def Slideshow(request):
    cards = [
        "summary-slides/ticket-amount.html",
        "summary-slides/origin-slide.html",
        "summary-slides/ticket-percentage.html",
        "summary-slides/find-the-truth.html",
        "summary-slides/animated-ticket-amount.html"
    ]
    data = ["summary-slides/begin-slide.html"]
    for _ in range(3):
        index = random.randrange(len(cards))
        data.append({"Card": cards[index], "Toggled": False})
        cards.pop(index)

    return render(request, "summary.html", {"Cards": data})

# ALL STARTS FROM HERE


def LoginPage(request):
    if request.user.is_authenticated:
        return redirect("/index")
    return render(request, "dashboard/login/login.html", {})


def SignUp(request):
    return HttpResponse(True)


@csrf_exempt
def SignIn(request):
    user = authenticate(
        username=request.POST["username"], password=request.POST["password"]
    )
    if user is not None:
        login(request, user)
        return redirect("/index")
    else:
        return HttpResponse(False)


def SignOut(request):
    logout(request)
    return redirect("/login/")


def ChangePassword(request):
    user = User.objects.get(username=request.POST.get("username"))
    user.set_password(request.POST.get("password"))
    user.save()
    return HttpResponse(True)


def CreateAccount(request):
    user = User.objects.create_user(
        request.POST.get("username"),
        request.POST.get("email"),
        request.POST.get("password"),
    )
    # user.last_name = "Lennon"
    user.save()

    return HttpResponse(user)


# END LOGIN

# CSV GENERATION
def GenerateCSV(request):
    MockMaker.GenerateMockData()
    return HttpResponse(False)


# END CSV


def Statistics(request):
    return HttpResponse("Bruh")


def Settings(request):
    return HttpResponse("Download RAM")


# populates the dashboard with a list of organizers waiting for their Eventix Wrapped
def GetOrganizers(request):
    return JsonResponse(APIMockService.GetOrganizersWithNoWrap(12))


def Stef(request):
    bruh = get_events_name_list()
    raise Exception()

    return HttpResponse(

    )


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
