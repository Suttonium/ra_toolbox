from django.contrib import admin

# Register your models here.
from accounts.models import User, Student, ResidentAssistant, HallDirector, DeskAccount

admin.site.register(User)
admin.site.register(Student)
admin.site.register(ResidentAssistant)
admin.site.register(HallDirector)
admin.site.register(DeskAccount)
