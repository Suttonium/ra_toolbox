from django.contrib import admin

# Register your models here.
from desklogs.models import *

admin.site.register(GuestLog)
admin.site.register(GuestLogEntry)
admin.site.register(EquipmentLog)
admin.site.register(EquipmentLogEntry)
