from django.urls import path
from . import views

urlpatterns = [
    path("panel", views.panel, name="Panel"),
    path("receiveJSON", views.receiveJSON),
]
