from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render


# Create your views here.
from django.views.generic import ListView

from desklogs.models import GuestLogEntry


class GuestLogEntryListView(LoginRequiredMixin, ListView):
    model = GuestLogEntry
