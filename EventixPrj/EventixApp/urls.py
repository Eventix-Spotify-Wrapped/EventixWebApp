from django.urls import path
from . import views

urlpatterns = [
    path("panel/", views.panel, name="Panel"),
    path("xrDemo/", views.xrDemo, name="xrDemo"),
    path("eventNumbers/", views.eventNumbers, name="eventNumbers"),
    path("ticketsTotal/", views.ticketsTotal, name="ticketsTotal"),
    path("peakSaleDay/", views.peakSaleDay, name="peakSaleDay"),
    path("peakSaleMonth/", views.peakSaleMonth, name="peakSaleMonth"),
    path("showUp/", views.showUp, name="showUp"),
    path("visitorsInfo/", views.visitorsInfo, name="visitorsInfo"),
    path("visitorsInfoModified/", views.visitorsInfoModified,
         name="visitorsInfoModified"),
    path("authorize/", views.Authorize),
    path("test/", views.GetEventixAccountId),
    path("callback/", views.Callback),
    path("visitorsInfo2/", views.visitorsInfo2, name="visitorsInfo2"),
    path("visitorsAge/", views.visitorsAge, name="visitorsAge"),
    path("visitorsAge2/", views.visitorsAge2, name="visitorsAge2"),
    path("customerLoyalty/", views.customerLoyalty, name="customerLoyalty"),
    path("", views.Summary, name="Panel"),
    path("summary2/<account_id>", views.Summary2),
    path("create/", views.Create),
    path("finalize/", views.Finalize),
    path("editsummary/<guid>", views.EditSummary),
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
    path("savewrap/", views.SaveWrap),
    path("addorganizerpage/", views.AddOrganizerPage),
    path("addorganizer/", views.AddOrganizer)
]
