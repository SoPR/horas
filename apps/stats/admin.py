from django.contrib import admin

from .models import Stat


class StatAdmin(admin.ModelAdmin):
    list_display = ("name", "count", "date_created")
    list_filter = ("name",)


admin.site.register(Stat, StatAdmin)
