from django.contrib import admin
from . import models
from  django.contrib.auth.models  import  Group, User
# Register your models here.

admin.site.register(models.CovidData)

admin.site.site_header = "Covid Data"
admin.site.site_title = "Assignment 1"

admin.site.unregister(Group)

class dataAdmin (admin.ModelAdmin):
    list_display = (
        "Country",
        "Confirmed",
        "New_cases",
        "Deaths",
        "Recovered",
    )