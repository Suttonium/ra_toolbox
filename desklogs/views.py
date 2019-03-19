import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView

from desklogs.models import GuestLogEntry, GuestLog
from django.db.models import Q


class GuestLogEntryListView(LoginRequiredMixin, ListView):
    model = GuestLogEntry
    template_name = 'desklogs/guestlog.html'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = self.request.user
        context['user'] = user
        context['guestlog'] = user.guestlog
        checked_in_list = user.guestlog.guestlogentry_set.filter(guest_checked_in=True)
        checked_out_list = user.guestlog.guestlogentry_set.filter(guest_checked_in=False)
        context['guestlog_entries'] = checked_in_list | checked_out_list
        for entry in user.guestlog.guestlogentry_set.all():
            if not entry.host_name or not entry.guest_name:
                context['disable_creation'] = True
        return context


class CreateBlankGuestLogEntry(View):
    template_name = 'desklogs/create_guestlog_entry_response.html'

    def get(self, request):
        guestlog_pk = request.GET.get('guestlog_pk')
        guestlog = GuestLog.objects.get(pk=guestlog_pk)
        now = datetime.datetime.now()
        time = '{0}:{1}:{2}'.format(str(now.hour),
                                    '0' + str(now.minute) if len(str(now.minute)) == 1 else str(now.minute),
                                    '0' + str(now.second) if len(str(now.second)) == 1 else str(now.second))
        date = '{0}-{1}-{2}'.format(str(now.month), str(now.day), str(now.year))
        GuestLogEntry.objects.create(guest_log=guestlog, time_in=time, date_in=date)

        user = self.request.user
        disable = False
        for entry in user.guestlog.guestlogentry_set.all():
            if entry.host_name is None or entry.guest_name is None:
                disable = True

        checked_in_list = user.guestlog.guestlogentry_set.filter(guest_checked_in=True)
        checked_out_list = user.guestlog.guestlogentry_set.filter(guest_checked_in=False)

        context = {
            'user': self.request.user, 'guestlog': guestlog,
            'guestlog_entries': checked_in_list | checked_out_list,
            'disable_creation': True if disable else False
        }
        return render(request, self.template_name, context)


class UpdateGuestlogEntry(View):
    template_name = 'desklogs/create_guestlog_entry_response.html'

    def get(self, request):
        guestlog_pk = request.GET.get('guestlog_pk')
        guestlog = GuestLog.objects.get(pk=guestlog_pk)

        entry_pk = request.GET.get('current_entry_being_updated_pk')
        host_name = request.GET.get('host_name')
        guest_name = request.GET.get('guest_name')
        entry = GuestLogEntry.objects.get(pk=entry_pk)
        entry.host_name = host_name
        entry.guest_name = guest_name
        entry.save()

        user = self.request.user
        disable = False
        for entry in user.guestlog.guestlogentry_set.all():
            if entry.host_name is None or entry.guest_name is None:
                disable = True

        checked_in_list = user.guestlog.guestlogentry_set.filter(guest_checked_in=True)
        checked_out_list = user.guestlog.guestlogentry_set.filter(guest_checked_in=False)

        context = {
            'user': self.request.user, 'guestlog': guestlog,
            'guestlog_entries': checked_in_list | checked_out_list,
            'disable_creation': True if disable else False
        }

        return render(request, self.template_name, context)


class CheckoutGuestlogEntry(View):
    template_name = 'desklogs/create_guestlog_entry_response.html'

    def get(self, request):
        guestlog_pk = request.GET.get('guestlog_pk')
        guestlog = GuestLog.objects.get(pk=guestlog_pk)
        entry_pk = request.GET.get('current_entry_being_updated_pk')
        entry = GuestLogEntry.objects.get(pk=entry_pk)
        now = datetime.datetime.now()
        time = '{0}:{1}:{2}'.format(str(now.hour),
                                    '0' + str(now.minute) if len(str(now.minute)) == 1 else str(now.minute),
                                    '0' + str(now.second) if len(str(now.second)) == 1 else str(now.second))
        date = '{0}-{1}-{2}'.format(str(now.month), str(now.day), str(now.year))
        entry.time_out = time
        entry.date_out = date
        entry.guest_checked_in = False
        entry.save()

        user = self.request.user
        disable = False
        for entry in user.guestlog.guestlogentry_set.all():
            if entry.host_name is None or entry.guest_name is None:
                disable = True

        checked_in_list = user.guestlog.guestlogentry_set.filter(guest_checked_in=True)
        checked_out_list = user.guestlog.guestlogentry_set.filter(guest_checked_in=False)

        context = {
            'user': self.request.user, 'guestlog': guestlog,
            'guestlog_entries': checked_in_list | checked_out_list,
            'disable_creation': True if disable else False
        }

        return render(request, self.template_name, context)


class FilterGuestlogEntries(View):
    template_name = 'desklogs/create_guestlog_entry_response.html'

    def get(self, request):
        query = request.GET.get('query')
        guestlog_pk = request.GET.get('guestlog_pk')
        guestlog = GuestLog.objects.get(pk=guestlog_pk)
        entries = guestlog.guestlogentry_set.filter(Q(host_name__contains=query) | Q(guest_name__contains=query))

        user = self.request.user
        disable = False
        for entry in user.guestlog.guestlogentry_set.all():
            if entry.host_name is None or entry.guest_name is None:
                disable = True

        context = {
            'user': self.request.user, 'guestlog': guestlog,
            'guestlog_entries': entries,
            'disable_creation': True if disable else False
        }

        return render(request, self.template_name, context)
