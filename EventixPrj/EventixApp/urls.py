from django.urls import path
from . import views

urlpatterns = [
    path("panel/", views.panel, name="Panel"),
    path("eventNumbers/", views.eventNumbers),
    path("ticketsTotal/", views.ticketsTotal),
    path("peakSaleDay/", views.peakSaleDay),
    path("peakSaleMonth/", views.peakSaleMonth),
    path("showUp/", views.showUp),
    path("visitorsInfo/", views.visitorsInfo),
    path("visitorsInfoModified/", views.visitorsInfoModified),
    path("visitorsInfo2/", views.visitorsInfo2),
    path("visitorsAge/", views.visitorsAge),
    path("visitorsAge2/", views.visitorsAge2),
    path("customerLoyalty/", views.customerLoyalty),
    path("", views.Summary, name="Panel"),
    path("create/", views.Create),
    path("finalize/", views.Finalize),
    path("event/<guid>/<event_name>/", views.Event),
    path("index/", views.Index),
    path("login/", views.LoginPage),
    path("login/signup", views.SignUp),
    path("login/signin", views.SignIn),
    path("login/signout", views.SignOut),
    path("login/changepassword/", views.ChangePassword),
    path("login/createaccount/", views.CreateAccount),
    path("statistics/", views.Statistics),
    path("settings/", views.Settings),
    path("generateCSV/", views.GenerateCSV),
    path("stef/", views.Stef),
    path("slideshow/", views.Slideshow),
    path("savewrap/", views.SaveWrap)
]
