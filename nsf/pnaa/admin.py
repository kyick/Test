from django.contrib import admin
from .models import Route
from pnaa.models import Cell

# Register your models here.
admin.site.register(Route)
admin.site.register(Cell)
