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
<<<<<<< HEAD
<<<<<<< HEAD


=======
import pdb
>>>>>>> d99b24c (moved and renamed)
=======
import pdb
>>>>>>> 78a248da5a06d6f485f310a382bffcd0c6394470
# Create your views here.


def panel(request):
    template = loader.get_template("dev/panel.html")
    return HttpResponse(template.render())


def Sprint2Demo(request):
    context = ["20.025", "69", "TQ Campus", "Wish outdoor", "85"]
    return render(request, "demo/Sprint2.html", {"context": context})


def Index(request):
    if not request.user.is_authenticated:
        return redirect("/login/")

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
    return render(request, "dashboard/event.html", {"Name": guid})


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
<<<<<<< HEAD
<<<<<<< HEAD
    list_of_objects = create_list_of_objects(
        "C:/Users/tepap/Desktop/Eventix/EventixWebApp/ticketing_export_2023_03_24_11_27_16.csv")
    most_popular_city_event1 = calculate_city_percentage(list_of_objects, 'Data preview 2016')
    most_popular_city_event2 = calculate_city_percentage(list_of_objects, 'Data preview 2017')
    showup_percentage_event1 = calculate_showup_percentage(list_of_objects, 'Data preview 2016')
    showup_percentage_event2 = calculate_showup_percentage(list_of_objects, 'Data preview 2017')
    average_age_event1 = calculate_average_age(list_of_objects, 'Data preview 2016')
    average_age_event2 = calculate_average_age(list_of_objects, 'Data preview 2017')
    gender_event1 = calculate_gender_percentage(list_of_objects, 'Data preview 2016')
    gender_event2 = calculate_gender_percentage(list_of_objects, 'Data preview 2017')
    total_revenue_event1 = calculate_total_revenue_event(list_of_objects, 'Data preview 2016')
    average_ticket_price_event1 = calculate_average_ticket_price(list_of_objects, 'Data preview 2016')
    total_revenue_event2 = calculate_total_revenue_event(list_of_objects, 'Data preview 2017')
    average_ticket_price_event2 = calculate_average_ticket_price(list_of_objects, 'Data preview 2017')
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
=======
=======
>>>>>>> 78a248da5a06d6f485f310a382bffcd0c6394470
    bruh = CSV_Reader.create_transactions_from_csv(
        "mock.csv"
    )
    raise Exception()

    return HttpResponse(

    )
<<<<<<< HEAD
>>>>>>> d99b24c (moved and renamed)
=======
>>>>>>> 78a248da5a06d6f485f310a382bffcd0c6394470


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
