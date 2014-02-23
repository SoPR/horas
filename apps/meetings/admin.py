from django.contrib import admin

from .models import Meeting


class MeetingAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'protege', 'cancelled_by', 'datetime')


admin.site.register(Meeting, MeetingAdmin)
