from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'get_html_photo', 'url')
    list_display_links = ('title',)


    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}', width=50>")

    get_html_photo.short_description = 'Миниатюра'


admin.site.register(Project, ProjectAdmin)
admin.site.site_title = ('Админ-панель сайта-портфолио')
