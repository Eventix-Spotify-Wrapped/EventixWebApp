from django.urls import path
from . import views

urlpatterns = [
    path("panel/", views.panel, name="Panel"),
    path("", views.Summary, name="Panel"),
    path("summary2/<account_id>", views.Summary2),
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
    path("savewrap/", views.SaveWrap),
]
