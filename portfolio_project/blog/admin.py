from django.contrib import admin
from .models import *


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title',  'time_create')
    list_display_links = ('title',)



admin.site.register(Blog,PortfolioAdmin)