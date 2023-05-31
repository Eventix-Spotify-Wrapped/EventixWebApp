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
from EventixApp.models import Wrap, Card, CardTemplate
import pdb
import random
from . import StatsCalculator
# Create your views here.


def panel(request):
    template = loader.get_template("dev/panel.html")
    return HttpResponse(template.render())


def Summary(request):
    list_of_objects = StatsCalculator.StatsCalculate.create_list_of_objects(
        "ticketing_export_2023_03_24_11_27_16.csv")
    total_revenue_event = StatsCalculator.StatsCalculate.calculate_total_revenue_event(
        list_of_objects, "Data preview 2016")
    event = {
        "totalRevenue": total_revenue_event,
        "name": "Wish Outdoor",
        "eventsOrganised": 8,
        "visitorPercentage": 85,
        "totalOfVisitors": 58472,
        "ticketSaleAmount": 20025,
        "ticketSalePercentage": 92,
        "cityMostVisitors": "Eindhoven",
        "provinceMostVisitors": "Noord-Brabant",
        "countryMostVisitors": "The Netherlands"
    }
    return render(request, "summary.html", {"event": event})


def Index(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    total_events_nameguid_keypair = StatsCalculator.StatsCalculate.get_events_name_guid_keypair()
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
    cards = list(CardTemplate.objects.values_list())
    # list_of_objects = StatsCalculator.StatsCalculate.create_list_of_objects(
    #    "mock.csv")
    # most_popular_city_event = StatsCalculator.StatsCalculate.calculate_city_percentage(
    #    list_of_objects, event_name)
    # showup_percentage_event = StatsCalculator.StatsCalculate.calculate_showup_percentage(
    #    list_of_objects, event_name)
    # average_age_event = StatsCalculator.StatsCalculate.calculate_average_age(
    #    list_of_objects, event_name)
    # gender_event = StatsCalculator.StatsCalculate.calculate_gender_percentage(
    #    list_of_objects, event_name)
    # total_revenue_event = StatsCalculator.StatsCalculate.calculate_total_revenue_event(
    #    list_of_objects, event_name)
    # average_ticket_price_event = StatsCalculator.StatsCalculate.calculate_average_ticket_price(
    #    list_of_objects, event_name)
    name = event_name
    data = []
    completed_wraps_account_ids = Wrap.objects.values_list(
        'owner_account_id', flat=True)
    preselected_cards = []
    overwrite = False
    for owner in completed_wraps_account_ids:
        if (owner in guid):
            preselected_cards = list(Card.objects.all().values("html_path").filter(
                wrap=Wrap.objects.get(owner_account_id=guid)).values())
    if (len(preselected_cards) > 0):
        overwrite = True
  #  raise MyException()
    for _ in range(len(cards)):
        if (len(preselected_cards) > 0):
            data.append(
                {"id": preselected_cards[0]["html_path"],
                    "Name": preselected_cards[0]["html_path"].split('/')[1].split('.')[0].replace('-', ' ').title(),
                 "imagePreview": preselected_cards[0]["thumbnail_path"],
                 "Toggled": True, })
            for card in cards:
                if (card[2] in preselected_cards[0]["html_path"]):
                    cards.remove(card)
            preselected_cards.pop(0)
            continue
        index = random.randrange(len(cards))
        data.append({"id": cards[index][2],
                     "Name": cards[index][2].split(
            '/')[1].split('.')[0].replace('-', ' ').title(),
            "imagePreview": cards[index][1],
            "Toggled": False})
        cards.pop(index)
  #  raise MyException('msg here')

    return render(request, "dashboard/event.html", {"Name": name, "Guid": guid, "Overwrite": overwrite, "Cards": data})


def CalculateInsightForCardName(cardname):
    bruh = ["Template"]
    return bruh[0]
    funct = getattr(StatsCalculator.StatsCalculate, cardname)
    result = funct()
    return result


class MyException(Exception):
    pass


def SaveWrap(request):
    cards = request.GET.getlist("cards")
    owner = request.GET.get("owner")

    if (not Wrap.objects.filter(owner_account_id=owner).exists()):
        w = Wrap(
            owner_account_id=owner,
        )
        w.save()
        for card in cards:
            c = Card(
                wrap=w,
                html_path=card,
                thumbnail_path=CardTemplate.objects.all().values(
                    "thumbnail_path").get(html_path=card)["thumbnail_path"],
                context=["hey", "sup"]
            )
            c.save()
    else:
        w = Wrap.objects.get(owner_account_id=owner)
        w.save()
        Card.objects.filter(wrap=w).delete()
        for card in cards:
            c = Card(
                wrap=w,
                html_path=card,
                thumbnail_path=CardTemplate.objects.all().values(
                    "thumbnail_path").get(html_path=card)["thumbnail_path"],
                context=["hey", "sup"]
            )
            c.save()
    return HttpResponse(print(w))


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
    list_of_objects = StatsCalculator.StatsCalculate.create_list_of_objects(
        "ticketing_export_2023_03_24_11_27_16.csv")
    most_popular_city_event1 = StatsCalculator.StatsCalculate.calculate_city_percentage(
        list_of_objects, 'Data preview 2016')
    most_popular_city_event2 = StatsCalculator.StatsCalculate.calculate_city_percentage(
        list_of_objects, 'Data preview 2017')
    showup_percentage_event1 = StatsCalculator.StatsCalculate.calculate_showup_percentage(
        list_of_objects, 'Data preview 2016')
    showup_percentage_event2 = StatsCalculator.StatsCalculate.calculate_showup_percentage(
        list_of_objects, 'Data preview 2017')
    average_age_event1 = StatsCalculator.StatsCalculate.calculate_average_age(
        list_of_objects, 'Data preview 2016')
    average_age_event2 = StatsCalculator.StatsCalculate.calculate_average_age(
        list_of_objects, 'Data preview 2017')
    gender_event1 = StatsCalculator.StatsCalculate.calculate_gender_percentage(
        list_of_objects, 'Data preview 2016')
    gender_event2 = StatsCalculator.StatsCalculate.calculate_gender_percentage(
        list_of_objects, 'Data preview 2017')
    total_revenue_event1 = StatsCalculator.StatsCalculate.calculate_total_revenue_event(
        list_of_objects, 'Data preview 2016')
    average_ticket_price_event1 = StatsCalculator.StatsCalculate.calculate_average_ticket_price(
        list_of_objects, 'Data preview 2016')
    total_revenue_event2 = StatsCalculator.StatsCalculate.calculate_total_revenue_event(
        list_of_objects, 'Data preview 2017')
    average_ticket_price_event2 = StatsCalculator.StatsCalculate.calculate_average_ticket_price(
        list_of_objects, 'Data preview 2017')
    context = {'total_revenue1': total_revenue_event1, 'average_ticket_price1': average_ticket_price_event1,
               'total_revenue2': total_revenue_event2, 'average_ticket_price2': average_ticket_price_event2,
               'gender_event1_male': gender_event1[0], 'gender_event1_female': gender_event1[1],
               'gender_event2_male': gender_event2[0],
               'gender_event2_female': gender_event2[1], 'average_age_event1': average_age_event1,
               'average_age_event2': average_age_event2, 'showup_percentage_event1': showup_percentage_event1,
               'showup_percentage_event2': showup_percentage_event2,
               'most_popular_city_event1': most_popular_city_event1,
               'most_popular_city_event2': most_popular_city_event2}
    return render(request, 'my_template.html', context)


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
