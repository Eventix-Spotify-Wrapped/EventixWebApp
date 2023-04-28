from django.urls import path
from . import views

urlpatterns = [
    path("panel/", views.panel, name="Panel"),
    path("sprint2demo/", views.Sprint2Demo, name="Panel"),
    path("create/", views.Create),
    path("finalize/", views.Finalize),
    path("event/<guid>/", views.Event),
    path("index/", views.Index),
    path("login/", views.LoginPage),
    path("login/signup", views.SignUp),
    path("login/signin", views.SignIn),
    path("login/signout", views.SignOut),
    path("login/changepassword/", views.ChangePassword),
    path("login/createaccount/", views.CreateAccount),
    path("statistics/", views.Statistics),
    path("settings/", views.Settings),
]
