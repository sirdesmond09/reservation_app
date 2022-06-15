from django.contrib import admin
from .models import Rental, Reservation

# Register your models here.

admin.site.register([Rental, Reservation])
