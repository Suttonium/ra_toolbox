from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from desklogs.models import GuestLogEntry


class GuestLogEntryListView(LoginRequiredMixin, ListView):
    model = GuestLogEntry
    template_name = 'desklogs/desklog.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = self.request.user
        context['user'] = user
        context['guestlog'] = user.guestlog
        context['guestlog_entries'] = user.guestlog.guestlogentry_set.all()
        return context
