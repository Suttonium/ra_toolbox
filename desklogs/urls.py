from django.urls import path
from desklogs.views import *

urlpatterns = [
    path('guest_log/', GuestLogEntryListView.as_view(), name='guest-log'),
]
