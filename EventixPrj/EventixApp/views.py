from faker import Faker
import qrcode
import base64
from io import BytesIO
from PIL import Image
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
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
    redirect = HttpResponseRedirect('/authorize/')
    redirect.set_cookie('account_id', account_id)
    if (access_token is None):
        return redirect
    if (access_token == "None"):
        return redirect
    if (GetEventixAccountId(request) not in account_id):
        return HttpResponse("Acess denied!")
    if not Wrap.objects.filter(owner_account_id=account_id).exists():
        return HttpResponse("Sorry, your wrap is not ready!")
    wrap = Wrap.objects.get(owner_account_id=account_id)
    cards = list(Card.objects.filter(wrap=wrap).values("html_path"))
    context = list(Card.objects.filter(wrap=wrap).values("context"))
    # list_of_objects = StatsCalculator.StatsCalculate.create_list_of_objects(
    #     "ticketing_export_2023_03_24_11_27_16.csv")
    # total_revenue_event = StatsCalculator.StatsCalculate.calculate_total_revenue_event(
    #     list_of_objects, "Data preview 2016")

    event = {
        "name": wrap.organizer_name,
        "totalRevenue": GetContext(wrap, "summary-slides/animated-ticket-sale-amount.html"),
        "eventsOrganised": GetContext(wrap, "summary-slides/events-organised.html"),
        "visitorPercentage": GetContext(wrap, "summary-slides/visitor-origins.html"),
        "totalOfVisitors": GetContext(wrap, "summary-slides/end-overview.html", 0),
        "countryMostVisitors": GetContext(wrap, "summary-slides/end-overview.html", 1),
        "cityMostVisitors": GetContext(wrap, "summary-slides/end-overview.html", 2),
        "provinceMostVisitors": GetContext(wrap, "summary-slides/end-overview.html", 3),
        "ticketSaleAmount": GetContext(wrap, "summary-slides/ticket-sale-amount.html"),
        "ticketSalePercentage": GetContext(wrap, "summary-slides/ticket-sale-percentage.html"),
        "averageAgeOfVisitors": GetContext(wrap, "summary-slides/average-age-visitors.html"),
        "dayOfMonthMostTicketSales": GetContext(wrap, "summary-slides/date-most-ticket-sales.html", 0),
        "monthMostTicketSales": GetContext(wrap, "summary-slides/date-most-ticket-sales.html", 1)
    }

    # slides = list(cards)
    slides = []
    for card in cards:
        slides.append(
            {"html": card["html_path"], "context": context[cards.index(card)]["context"]})
    # raise MyException()
   # raise MyException()
    return render(request, "summary2.html", {"event": event, "slides": slides})


def GetContext(wrap, html_path, contextIndex=0):
    awesome = Card.objects.filter(wrap=wrap, html_path=html_path)
    if not awesome:
        return None
    context = list(awesome)[0].context

    if ("|" in context):
        return context.split('|')[contextIndex]
    return context


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


clientid = 'WctSZaDe8Q6O65dQ66mXMlQ0TkTt7GC2Ebv3wDCk'
clientsecret = "KUJmrVOYTKqKyGaUCGWzGmy43gmgnv9e2puZU84y"


def GetEventixAccountId(request):
    access_token = request.COOKIES.get('access_token', None)
    if (access_token is None):
        return redirect("/authorize/")
    headers = {'Authorization': 'Bearer ' + access_token}
    req = requests.get("https://auth.openticket.tech/user/me", headers=headers)

    return json.loads(req.text)["guid"]


def Authorize(request):
    url = "https://auth.openticket.tech/token/authorize?response_type=code&client_id=WctSZaDe8Q6O65dQ66mXMlQ0TkTt7GC2Ebv3wDCk&state=sgaedwawd&redirect_uri=https://eventix-wrapped.ngrok.app/callback"
    return redirect(url)


def Callback(request):
    account_id = request.COOKIES.get('account_id', None)
    if (account_id is None):
        return redirect('/')
    code = request.GET.get('code')
    redir = "/summary/" + account_id
    data = {
        'grant_type': 'authorization_code',
        "code": code,
        "client_id": clientid,
        "client_secret": clientsecret,
        "redirect_uri": "https://eventix-wrapped.ngrok.app/callback"
    }

    req = requests.post("https://auth.openticket.tech/token", data)
    text = req.json()
    token = None
    if ("token_type" in text):
        token = text["access_token"]
    resp = HttpResponseRedirect(redir)
    resp.set_cookie('access_token', token)
  #  raise MyException()
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


def Index(request):
    # fake = Faker()

    # return HttpResponse(fake.date_time_between(
   #     start_date='-1y', end_date='now'))
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
                        {"Wrapped": True, "Guid": ng_kp["Guid"],
                         "Organizer": StatsCalculator.StatsCalculate.get_organizer_name_by_guid(ng_kp["Guid"])})
                    alreadyAdded = True
            if (not alreadyAdded):
                data.insert(
                    0, {"Wrapped": False, "Guid": ng_kp["Guid"],
                        "Organizer": StatsCalculator.StatsCalculate.get_organizer_name_by_guid(ng_kp["Guid"])})
    #  raise MyException()

    return render(
        request,
        "dashboard/index.html",
        {
            "events":
                data,
        },
    )


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
    organizer_name = request.GET.get("organizer")
    context = request.GET.getlist("context")

    host = request.get_host()
    url = f"https://{host}/summary/{owner}"

    for card in cards:
        if ("end-overview.html" in card):
            c = context.pop(cards.index(card))
            context.append(c)
            cards.remove(card)
            cards.append(card)

    if (not Wrap.objects.filter(owner_account_id=owner).exists()):
        w = Wrap(
            owner_account_id=owner,
            organizer_name=organizer_name
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
    send_mail(
        'Your Wrap is Ready!',
        f'There is a lot of fun involved! You can view it at {url}',
        'cs.eventix.dev.test@gmail.com',
        ['andisavauserul@gmail.com'],
        fail_silently=False,
    )

    return redirect("/editsummary/" + owner)


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
        "averageAgeOfVisitors": 23,
        "cityMostVisitors": "Eindhoven",
        "provinceMostVisitors": "Noord-Brabant",
        "countryMostVisitors": "The Netherlands"
    }
    return render(request, "summary.html", {"event": event})


def AddOrganizerPage(request):
    return render(request, "demo/addOrganizer.html")


def visitorsInfo2(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/visitorsInfo2.html", {"context": context})


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


def AddOrganizer(request):
    obj = {"Organizer": request.GET.get("organizer"),
           "Events": request.GET.getlist("events")}
    MockMaker.GenerateMockDataSpecific(obj)

    return HttpResponse(obj["Organizer"])


def visitorsAge(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/visitorsAge.html", {"context": context})


def customerLoyalty(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/customerLoyalty.html", {"context": context})


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


def visitorsAge2(request):
    # change the context during develop
    context = []
    return render(request, "demo/xinru/visitorsAge2.html", {"context": context})


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
                 "Toggled": True,
                 "Context": CalculateFunction(preselected_cards[0]["html_path"], guid)})
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
                     "Toggled": False,
                     "Context": CalculateFunction(cards[index][2], guid)})
        cards.pop(index)

    return render(request, "dashboard/event.html",
                  {"Organizer": info["Organizer"], "Events": info["Events"], "Guid": guid, "Overwrite": overwrite,
                   "Cards": data, "qr_code": qr_base64})


def CalculateFunction(html_path, guid):
    value = None
    list_of_objects = StatsCalculator.StatsCalculate.create_list_of_objects(
        "ticketing_export_2023_03_24_11_27_16.csv")
    if ("animated-ticket-sale-amount.html" in html_path):
        value = StatsCalculator.StatsCalculate.calculate_total_ticket_sells(
            list_of_objects, guid)
    elif ("average-age-visitors.html" in html_path):
        value = StatsCalculator.StatsCalculate.calculate_average_age(list_of_objects, guid)
    elif ("date-most-ticket-sales.html" in html_path):
        value = StatsCalculator.StatsCalculate.calculate_day_most_tickets_sold(
            list_of_objects, guid)
    elif ("end-overview.html" in html_path):
        visitors = StatsCalculator.StatsCalculate.calculate_total_visitors(
            list_of_objects, guid)
        most_popular_country = StatsCalculator.StatsCalculate.calculate_most_popular_country(
            list_of_objects, guid)
        most_popular_city = StatsCalculator.StatsCalculate.calculate_most_popular_city(
            list_of_objects, guid)
        most_popular_region = StatsCalculator.StatsCalculate.calculate_most_popular_province(
            list_of_objects, guid)
        value = '{visitors} | {most_popular_country[0]} | {most_popular_city} | {most_popular_region}' .format(
            visitors=visitors, most_popular_country=most_popular_country, most_popular_city=most_popular_city, most_popular_region=most_popular_region)
    elif ("events-organised.html" in html_path):
        value = "Events organised"
    elif ("find-the-truth.html" in html_path):
        value = "Find the truth"
    elif ("start-animation.html" in html_path):
        value = "Start animation"
    elif ("ticket-sale-amount.html" in html_path):
        value = "Ticket sale amount"
    elif ("ticket-sale-percentage.html" in html_path):
        value = StatsCalculator.StatsCalculate.calculate_showup_percentage(
            list_of_objects, guid)
    elif ("visitor-origins.html" in html_path):
        a = StatsCalculator.StatsCalculate.calculate_most_popular_country(
            list_of_objects, guid)
        value = '{a[0]} | {a[1]}' .format(a=a)

    return value


def CalculateInsightForCardName(cardname):
    bruh = ["Template"]
    return bruh[0]
    funct = getattr(StatsCalculator.StatsCalculate, cardname)
    result = funct()
    return result


class MyException(Exception):
    pass


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
        list_of_objects, '36a9179d-7c3a-4ccb-aa0c-83e4f484ea40')
    most_popular_city_event2 = StatsCalculator.StatsCalculate.calculate_city_percentage(
        list_of_objects, '14009dfa-b925-4e5f-ab8b-4aa077c04299')
    showup_percentage_event1 = StatsCalculator.StatsCalculate.calculate_showup_percentage(
        list_of_objects, '36a9179d-7c3a-4ccb-aa0c-83e4f484ea40')
    showup_percentage_event2 = StatsCalculator.StatsCalculate.calculate_showup_percentage(
        list_of_objects, '14009dfa-b925-4e5f-ab8b-4aa077c04299')
    average_age_event1 = StatsCalculator.StatsCalculate.calculate_average_age(
        list_of_objects, '36a9179d-7c3a-4ccb-aa0c-83e4f484ea40')
    average_age_event2 = StatsCalculator.StatsCalculate.calculate_average_age(
        list_of_objects, '14009dfa-b925-4e5f-ab8b-4aa077c04299')
    gender_event1 = StatsCalculator.StatsCalculate.calculate_gender_percentage(
        list_of_objects, '36a9179d-7c3a-4ccb-aa0c-83e4f484ea40')
    gender_event2 = StatsCalculator.StatsCalculate.calculate_gender_percentage(
        list_of_objects, '14009dfa-b925-4e5f-ab8b-4aa077c04299')
    total_revenue_event1 = StatsCalculator.StatsCalculate.calculate_total_revenue_event(
        list_of_objects, '36a9179d-7c3a-4ccb-aa0c-83e4f484ea40')
    average_ticket_price_event1 = StatsCalculator.StatsCalculate.calculate_average_ticket_price(
        list_of_objects, '36a9179d-7c3a-4ccb-aa0c-83e4f484ea40')
    total_revenue_event2 = StatsCalculator.StatsCalculate.calculate_total_revenue_event(
        list_of_objects, '14009dfa-b925-4e5f-ab8b-4aa077c04299')
    average_ticket_price_event2 = StatsCalculator.StatsCalculate.calculate_average_ticket_price(
        list_of_objects, '14009dfa-b925-4e5f-ab8b-4aa077c04299')
    total_visitors_event1 = StatsCalculator.StatsCalculate.calculate_total_visitors(
        list_of_objects, '36a9179d-7c3a-4ccb-aa0c-83e4f484ea40')
    total_visitors_event2 = StatsCalculator.StatsCalculate.calculate_total_visitors(
        list_of_objects, '14009dfa-b925-4e5f-ab8b-4aa077c04299')
    events_per_year1 = StatsCalculator.StatsCalculate.calculate_events_per_year(
        list_of_objects, '36a9179d-7c3a-4ccb-aa0c-83e4f484ea40')
    events_per_year2 = StatsCalculator.StatsCalculate.calculate_events_per_year(
        list_of_objects, '14009dfa-b925-4e5f-ab8b-4aa077c04299')
    most_popular_country_event1 = StatsCalculator.StatsCalculate.calculate_most_popular_country(
        list_of_objects, '36a9179d-7c3a-4ccb-aa0c-83e4f484ea40')
    most_popular_country_event2 = StatsCalculator.StatsCalculate.calculate_most_popular_country(
        list_of_objects, '14009dfa-b925-4e5f-ab8b-4aa077c04299')
    ##############################
    day_most_tickets_sold1 = StatsCalculator.StatsCalculate.calculate_day_most_tickets_sold(
        list_of_objects, '36a9179d-7c3a-4ccb-aa0c-83e4f484ea40')
    day_most_tickets_sold2 = StatsCalculator.StatsCalculate.calculate_day_most_tickets_sold(
        list_of_objects, '14009dfa-b925-4e5f-ab8b-4aa077c04299')

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
