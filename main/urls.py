from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path("reservations/", views.get_reservations, name="reservation")
]
