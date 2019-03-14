import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView

from desklogs.models import GuestLogEntry, GuestLog


class GuestLogEntryListView(LoginRequiredMixin, ListView):
    model = GuestLogEntry
    template_name = 'desklogs/guestlog.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = self.request.user
        context['user'] = user
        context['guestlog'] = user.guestlog
        context['guestlog_entries'] = user.guestlog.guestlogentry_set.all()
        return context


class CreateBlankGuestLogEntry(View):
    template_name = 'desklogs/create_guestlog_entry_response.html'

    def get(self, request):
        guestlog_pk = request.GET.get('guestlog_pk')
        guestlog = GuestLog.objects.get(pk=guestlog_pk)
        now = datetime.datetime.now()
        time = '{0}:{1}:{2}'.format(str(now.hour), str(now.minute), str(now.second))
        date = '{0}-{1}-{2}'.format(str(now.month), str(now.day), str(now.year))
        GuestLogEntry.objects.create(guest_log=guestlog, time_in=time, date_in=date)
        context = {
            'user': self.request.user, 'guestlog': guestlog,
            'guestlog_entries': guestlog.guestlogentry_set.all()
        }
        return render(request, self.template_name, context)
