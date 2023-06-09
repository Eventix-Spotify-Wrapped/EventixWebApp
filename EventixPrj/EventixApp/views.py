import qrcode
import base64
from io import BytesIO
from PIL import Image
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .CSV_Reader import CSV_Reader
from django.contrib.auth import authenticate, logout, login
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.models import User
from .mock_maker_3000 import MockMaker
from EventixApp.models import Wrap, Card, CardTemplate
import pdb
import random
from . import StatsCalculator
import requests
import json
import urllib.parse

# Create your views here.


def panel(request):
    template = loader.get_template("dev/panel.html")
    return HttpResponse(template.render())


def Summary2(request, account_id):
    access_token = request.COOKIES.get('access_token', None)
    if (access_token is None):
        return redirect("/authorize/")
    if (GetEventixAccountId(request) not in account_id):
        return HttpResponse("Acess denied!")
    if not Wrap.objects.filter(owner_account_id=account_id).exists():
        return HttpResponse("Sorry, your wrap is not ready!")
    wrap = Wrap.objects.get(owner_account_id=account_id)
    cards = list(Card.objects.filter(wrap=wrap).values("html_path"))
    context = list(Card.objects.filter(wrap=wrap).values("context"))
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
        "averageAgeOfVisitors": 23,
        "cityMostVisitors": "Eindhoven",
        "provinceMostVisitors": "Noord-Brabant",
        "countryMostVisitors": "The Netherlands"
    }

    # slides = list(cards)
    slides = []
    for card in cards:
        slides.append(
            {"html": card["html_path"], "context": context[cards.index(card)]["context"]})
    # raise MyException()

    return render(request, "summary2.html", {"event": event, "slides": slides})


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
        "averageAgeOfVisitors": 23,
        "cityMostVisitors": "Eindhoven",
        "provinceMostVisitors": "Noord-Brabant",
        "countryMostVisitors": "The Netherlands"
    }
    return render(request, "summary.html", {"event": event})


clientid = 'vUG3sn7qbalfbTMXIwcIXoGjSAi718fZagzzFQX0'
clientsecret = "kTEN7muJIrgWKGgAyDDzaugWT0dTk3OdoV317xOL"


def Authorize(request):
    url = "https://auth.openticket.tech/token/authorize?response_type=code&client_id=vUG3sn7qbalfbTMXIwcIXoGjSAi718fZagzzFQX0&state=awddawdawdawd&redirect_uri=https%3A%2F%2Fbbe2-145-93-112-185.ngrok-free.app%2Fcallback"
    return redirect(url)


def GetEventixAccountId(request):
    access_token = request.COOKIES.get('access_token', None)
    if (access_token is None):
        return redirect("/authorize/")
    headers = {'Authorization': 'Bearer '+access_token}
    req = requests.get("https://auth.openticket.tech/user/me", headers=headers)

    return json.loads(req.text)["guid"]


def Callback(request):
    code = request.GET.get("code")
    data = {
        'grant_type': 'authorization_code',
        "code": code,
        "client_id": clientid,
        "client_secret": clientsecret,
        "redirect_uri": GetNgrokUri()+"/callback/"
    }

    req = requests.post("https://auth.openticket.tech/token", data)
    text = req.json()
    token = None
    if ("token_type" in text):
        token = text["access_token"]
    resp = HttpResponse(token)
    resp.set_cookie('access_token', token)

    return resp


def GetNgrokUri():
    req = requests.get("http://localhost:4040/api/tunnels")
    return json.loads(req.text)["tunnels"][0]["public_url"]


def AddOrganizerPage(request):

    return render(request, "demo/addOrganizer.html")


def AddOrganizer(request):
    obj = {"Organizer": request.GET.get("organizer"),
           "Events": request.GET.getlist("events")}
    MockMaker.GenerateMockDataSpecific(obj)

    return HttpResponse(obj["Organizer"])


def xrDemo(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/xrDemo.html", {"context": context})


def eventNumbers(request):
    # change the context during develop
    context = [
        "6" "It looks like you would like to be fully prepared for each one."]
    return render(request, "demo/xinru/eventNumbers.html", {"context": context})


def ticketsTotal(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/ticketsTotal.html", {"context": context})


def peakSaleDay(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/peakSale-D.html", {"context": context})


def peakSaleMonth(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/peakSale-M.html", {"context": context})


def showUp(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/showUp.html", {"context": context})


def visitorsInfo(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/visitorsInfo.html", {"context": context})


def visitorsInfoModified(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/visitorsInfoModified.html", {"context": context})


def visitorsInfo2(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/visitorsInfo2.html", {"context": context})


def visitorsAge(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/visitorsAge.html", {"context": context})


def visitorsAge2(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/visitorsAge2.html", {"context": context})


def customerLoyalty(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/customerLoyalty.html", {"context": context})


def xrDemo(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/xrDemo.html", {"context": context})


def eventNumbers(request):
    # change the context during develop
    context = [
        "6" "It looks like you would like to be fully prepared for each one."]
    return render(request, "demo/xinru/eventNumbers.html", {"context": context})


def ticketsTotal(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/ticketsTotal.html", {"context": context})


def peakSaleDay(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/peakSale-D.html", {"context": context})


def peakSaleMonth(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/peakSale-M.html", {"context": context})


def showUp(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/showUp.html", {"context": context})


def visitorsInfo(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/visitorsInfo.html", {"context": context})


def visitorsInfoModified(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/visitorsInfoModified.html", {"context": context})


def visitorsInfo2(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/visitorsInfo2.html", {"context": context})


def visitorsAge(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/visitorsAge.html", {"context": context})


def visitorsAge2(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/visitorsAge2.html", {"context": context})


def customerLoyalty(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/customerLoyalty.html", {"context": context})


def Index(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    total_organizers_nameguid_keypair = StatsCalculator.StatsCalculate.get_organizer_events_guid()
    completed_wraps = Wrap.objects.values_list('owner_account_id', flat=True)
    data = []

    for ng_kp in total_organizers_nameguid_keypair:
        alreadyAdded = False
        for dat in data:
            if (dat["Guid"] == ng_kp["Guid"]):
                alreadyAdded = True
        if (not alreadyAdded):
            for owner in completed_wraps:
                if (owner in ng_kp["Guid"]):
                    data.append(
                        {"Wrapped": True, "Guid": ng_kp["Guid"], "Organizer": StatsCalculator.StatsCalculate.get_organizer_name_by_guid(ng_kp["Guid"])})
                    alreadyAdded = True
            if (not alreadyAdded):
                data.insert(
                    0, {"Wrapped": False, "Guid": ng_kp["Guid"], "Organizer": StatsCalculator.StatsCalculate.get_organizer_name_by_guid(ng_kp["Guid"])})
  #  raise MyException()

    return render(
        request,
        "dashboard/index.html",
        {
            "events":
                data,
        },
    )


def EditSummary(request, guid):
    if not request.user.is_authenticated:
        return redirect("/login/")
    cards = list(CardTemplate.objects.values_list().order_by("id"))
    info = StatsCalculator.StatsCalculate.get_organizer_events_cards_guid_by_guid(
        guid)
    preselected_cards = []
    overwrite = False
    if ("Cards" in info.keys()):
        preselected_cards = info["Cards"]
    if (len(preselected_cards) > 0):
        overwrite = True

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
    data = []

    for _ in range(len(cards)):
        if (len(preselected_cards) > 0):
            data.append(
                {"id": preselected_cards[0]["html_path"],
                    "Name": preselected_cards[0]["html_path"].split('/')[1].split('.')[0].replace('-', ' ').title(),
                 "imagePreview": preselected_cards[0]["thumbnail_path"],
                 "Toggled": True, "Value": CalculateFunction(preselected_cards[0]["html_path"])})
            for card in cards:
                if (card[2] in preselected_cards[0]["html_path"]):
                    cards.remove(card)
            preselected_cards.pop(0)
            continue
        index = 0
        data.append({"id": cards[index][2],
                     "Name": cards[index][2].split(
            '/')[1].split('.')[0].replace('-', ' ').title(),
            "imagePreview": cards[index][1],
            "Toggled": False, "Value": CalculateFunction(cards[index][2])})
        cards.pop(index)
        bruh = data

    return render(request, "dashboard/event.html", {"Organizer": info["Organizer"], "Events": info["Events"], "Guid": guid, "Overwrite": overwrite, "Cards": data})


def CalculateFunction(html_path):
    value = None
    if ("animated-ticket-sale-amount.html" in html_path):
        value = "Ticket sale"
    elif ("average-age-visitors.html" in html_path):
        value = "Age visitors"
    elif ("date-most-ticket-sales.html" in html_path):
        value = "Most ticket sales"
    elif ("end-overview.html" in html_path):
        value = "End overview"
    elif ("events-organised.html" in html_path):
        value = "Events organised"
    elif ("find-the-truth.html" in html_path):
        value = "Find the truth"
    elif ("start-animation.html" in html_path):
        value = "Start animation"
    elif ("ticket-sale-amount.html" in html_path):
        value = "Ticket sale amount"
    elif ("ticket-sale-percentage.html" in html_path):
        value = "Ticket sale percentage"
    elif ("visitor-origins.html" in html_path):
        value = "Visitor origins"

    return value


def CalculateInsightForCardName(cardname):
    bruh = ["Template"]
    return bruh[0]
    funct = getattr(StatsCalculator.StatsCalculate, cardname)
    result = funct()
    return result


class MyException(Exception):
    pass


def SaveWrap(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    cards = request.GET.getlist("cards")
    owner = request.GET.get("owner")
    context = request.GET.getlist("context")

    for card in cards:
        if ("end-overview.html" in card):
            c = context.pop(cards.index(card))
            context.append(c)
            cards.remove(card)
            cards.append(card)

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
                context=context[cards.index(card)]
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
                context=context[cards.index(card)]
            )
            c.save()
    return redirect("/editsummary/"+owner)


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
# Create your views here.


def panel(request):
    template = loader.get_template("dev/panel.html")
    return HttpResponse(template.render())


def Summary2(request, account_id):
    if not Wrap.objects.filter(owner_account_id=account_id).exists():
        return HttpResponse("Sorry, your wrap is not ready!")
    wrap = Wrap.objects.get(owner_account_id=account_id)
    cards = Card.objects.filter(wrap=wrap).values("html_path")
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
        "averageAgeOfVisitors": 23,
        "cityMostVisitors": "Eindhoven",
        "provinceMostVisitors": "Noord-Brabant",
        "countryMostVisitors": "The Netherlands"
    }

    slides = list(cards)

    return render(request, "summary2.html", {"event": event, "slides": slides})


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
        "averageAgeOfVisitors": 23,
        "cityMostVisitors": "Eindhoven",
        "provinceMostVisitors": "Noord-Brabant",
        "countryMostVisitors": "The Netherlands"
    }
    return render(request, "summary.html", {"event": event})


def AddOrganizerPage(request):

    return render(request, "demo/addOrganizer.html")


def AddOrganizer(request):
    obj = {"Organizer": request.GET.get("organizer"),
           "Events": request.GET.getlist("events")}
    MockMaker.GenerateMockDataSpecific(obj)

    return HttpResponse(obj["Organizer"])


def xrDemo(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/xrDemo.html", {"context": context})


def eventNumbers(request):
    # change the context during develop
    context = [
        "6" "It looks like you would like to be fully prepared for each one."]
    return render(request, "demo/xinru/eventNumbers.html", {"context": context})


def ticketsTotal(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/ticketsTotal.html", {"context": context})


def peakSaleDay(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/peakSale-D.html", {"context": context})


def peakSaleMonth(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/peakSale-M.html", {"context": context})


def showUp(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/showUp.html", {"context": context})


def visitorsInfo(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/visitorsInfo.html", {"context": context})


def visitorsInfoModified(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/visitorsInfoModified.html", {"context": context})


def visitorsInfo2(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/visitorsInfo2.html", {"context": context})


def visitorsAge(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/visitorsAge.html", {"context": context})


def visitorsAge2(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/visitorsAge2.html", {"context": context})


def customerLoyalty(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/customerLoyalty.html", {"context": context})


def xrDemo(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/xrDemo.html", {"context": context})


def eventNumbers(request):
    # change the context during develop
    context = [
        "6" "It looks like you would like to be fully prepared for each one."]
    return render(request, "demo/xinru/eventNumbers.html", {"context": context})


def ticketsTotal(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/ticketsTotal.html", {"context": context})


def peakSaleDay(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/peakSale-D.html", {"context": context})


def peakSaleMonth(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/peakSale-M.html", {"context": context})


def showUp(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/showUp.html", {"context": context})


def visitorsInfo(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/visitorsInfo.html", {"context": context})


def visitorsInfoModified(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/visitorsInfoModified.html", {"context": context})


def visitorsInfo2(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/visitorsInfo2.html", {"context": context})


def visitorsAge(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/visitorsAge.html", {"context": context})


def visitorsAge2(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/visitorsAge2.html", {"context": context})


def customerLoyalty(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/customerLoyalty.html", {"context": context})


def Index(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    total_organizers_nameguid_keypair = StatsCalculator.StatsCalculate.get_organizer_events_guid()
    completed_wraps = Wrap.objects.values_list('owner_account_id', flat=True)
    data = []

    for ng_kp in total_organizers_nameguid_keypair:
        alreadyAdded = False
        for dat in data:
            if (dat["Guid"] == ng_kp["Guid"]):
                alreadyAdded = True
        if (not alreadyAdded):
            for owner in completed_wraps:
                if (owner in ng_kp["Guid"]):
                    data.append(
                        {"Wrapped": True, "Guid": ng_kp["Guid"], "Organizer": StatsCalculator.StatsCalculate.get_organizer_name_by_guid(ng_kp["Guid"])})
                    alreadyAdded = True
            if (not alreadyAdded):
                data.insert(
                    0, {"Wrapped": False, "Guid": ng_kp["Guid"], "Organizer": StatsCalculator.StatsCalculate.get_organizer_name_by_guid(ng_kp["Guid"])})
  #  raise MyException()

    return render(
        request,
        "dashboard/index.html",
        {
            "events":
                data,
        },
    )


def EditSummary(request, guid):
    if not request.user.is_authenticated:
        return redirect("/login/")
    cards = list(CardTemplate.objects.values_list().order_by("id"))
    info = StatsCalculator.StatsCalculate.get_organizer_events_cards_guid_by_guid(
        guid)
    preselected_cards = []
    overwrite = False
    if ("Cards" in info.keys()):
        preselected_cards = info["Cards"]
    if (len(preselected_cards) > 0):
        overwrite = True
    host = request.get_host()
    url = f"https://{host}/summary2/{guid}"

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=6,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a BytesIO object
    buffered = BytesIO()
    img.save(buffered, format="PNG")

    # Convert the BytesIO object to base64
    qr_base64 = base64.b64encode(buffered.getvalue()).decode()

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
    data = []

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
        index = 0
        data.append({"id": cards[index][2],
                     "Name": cards[index][2].split(
            '/')[1].split('.')[0].replace('-', ' ').title(),
            "imagePreview": cards[index][1],
            "Toggled": False})
        cards.pop(index)

    return render(request, "dashboard/event.html", {"Organizer": info["Organizer"], "Events": info["Events"], "Guid": guid, "Overwrite": overwrite, "Cards": data})


def CalculateInsightForCardName(cardname):
    bruh = ["Template"]
    return bruh[0]
    funct = getattr(StatsCalculator.StatsCalculate, cardname)
    result = funct()
    return result


class MyException(Exception):
    pass


def SaveWrap(request):
    if not request.user.is_authenticated:
        return redirect("/login/")
    cards = request.GET.getlist("cards")
    owner = request.GET.get("owner")
    host = request.get_host()
    url = f"https://{host}/summary2/{owner}"

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
    send_mail(
        'Your Wrap is Ready!',
        f'There is a lot of fun involved! You can view it at {url}',
        'cs.eventix.dev.test@gmail.com',
        ['john.eventix.dev.test@gmail.com'],
        fail_silently=False,
    )
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
    total_visitors_event1 = StatsCalculator.StatsCalculate.calculate_total_visitors(
        list_of_objects, 'Data preview 2016')
    total_visitors_event2 = StatsCalculator.StatsCalculate.calculate_total_visitors(
        list_of_objects, 'Data preview 2017')
    events_per_year1 = StatsCalculator.StatsCalculate.calculate_events_per_year(
        list_of_objects, 'Data preview 2016')
    events_per_year2 = StatsCalculator.StatsCalculate.calculate_events_per_year(
        list_of_objects, 'Data preview 2017')
    day_most_tickets_sold1 = StatsCalculator.StatsCalculate.calculate_day_most_tickets_sold(
        list_of_objects, 'Data preview 2016')
    day_most_tickets_sold2 = StatsCalculator.StatsCalculate.calculate_day_most_tickets_sold(
        list_of_objects, 'Data preview 2017')
    most_popular_country_event1 = StatsCalculator.StatsCalculate.calculate_most_popular_country(
        list_of_objects, 'Data preview 2016')
    most_popular_country_event2 = StatsCalculator.StatsCalculate.calculate_most_popular_country(
        list_of_objects, 'Data preview 2017')
    context = {'total_revenue1': total_revenue_event1, 'average_ticket_price1': average_ticket_price_event1,
               'total_revenue2': total_revenue_event2, 'average_ticket_price2': average_ticket_price_event2,
               'gender_event1_male': gender_event1[0], 'gender_event1_female': gender_event1[1],
               'gender_event2_male': gender_event2[0],
               'gender_event2_female': gender_event2[1], 'average_age_event1': average_age_event1,
               'average_age_event2': average_age_event2, 'showup_percentage_event1': showup_percentage_event1,
               'showup_percentage_event2': showup_percentage_event2,
               'most_popular_city_event1': most_popular_city_event1,
               'most_popular_city_event2': most_popular_city_event2,
               'total_visitors_event1': total_visitors_event1,
               'total_visitors_event2': total_visitors_event2, 'events_per_year1': events_per_year1,
               'events_per_year2': events_per_year2, 'day_most_tickets_sold1': day_most_tickets_sold1,
               'day_most_tickets_sold2': day_most_tickets_sold2,
               'most_popular_country_event1': most_popular_country_event1,
               'most_popular_country_event2': most_popular_country_event2}
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
