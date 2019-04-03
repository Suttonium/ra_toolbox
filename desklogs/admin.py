from django.contrib import admin

# Register your models here.
from desklogs.models import *

admin.site.register(GuestLog)
admin.site.register(GuestLogEntry)
admin.site.register(EquipmentLog)
admin.site.register(EquipmentLogEntry)
admin.site.register(LockoutLog)
admin.site.register(LockoutLogEntry)
admin.site.register(LockoutCode)
admin.site.register(PassDownLog)
admin.site.register(PassDownLogEntry)
