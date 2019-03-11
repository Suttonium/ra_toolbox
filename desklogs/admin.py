from django.contrib import admin

# Register your models here.
from desklogs.models import GuestLog, GuestLogEntry

admin.site.register(GuestLog)
admin.site.register(GuestLogEntry)
