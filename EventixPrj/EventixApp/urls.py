from django.urls import path
from . import views

urlpatterns = [
    path("panel", views.panel, name="Panel"),
    path("sprint2demo", views.Sprint2Demo, name="Panel"),
    path("receiveJSON", views.receiveJSON),
]
