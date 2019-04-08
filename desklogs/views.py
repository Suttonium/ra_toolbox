import datetime

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from desklogs.models import *


class UniversityRoster(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = 'desklogs/university_roster.html'
    permission_required = (
        'securityquestions.change_securityquestions', 'securityquestions.view_securityquestions'
    )

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['university_roster'] = User.objects.all().exclude(is_hall_director=True).exclude(
            is_desk_account=True).order_by('student_id')
        return context

    def test_func(self):
        return self.request.user.is_hall_director or self.request.user.is_desk_account


class FilterUniversityRoster(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, View):
    template_name = 'desklogs/university_roster_response.html'
    permission_required = (
        'securityquestions.change_securityquestions', 'securityquestions.view_securityquestions'
    )

    def get(self, request):
        query = request.GET.get('query')
        queryset = User.objects.all().exclude(is_hall_director=True).exclude(is_desk_account=True).filter(
            Q(email__contains=query) | Q(student_id__contains=query) | Q(
                student__residence_hall__name__contains=query)).order_by('student_id')

        context = {
            'university_roster': queryset
        }
        return render(request, self.template_name, context)

    def test_func(self):
        return self.request.user.is_hall_director or self.request.user.is_desk_account


class GuestLogEntryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = GuestLogEntry
    template_name = 'desklogs/guestlog.html'
    permission_required = (
        'desklogs.view_guestlog', 'desklogs.view_guestlogentry'
    )

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


class CreateBlankGuestLogEntry(LoginRequiredMixin, PermissionRequiredMixin, View):
    template_name = 'desklogs/create_guestlog_entry_response.html'
    permission_required = (
        'desklogs.add_guestlogentry'
    )

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


class UpdateGuestlogEntry(LoginRequiredMixin, PermissionRequiredMixin, View):
    template_name = 'desklogs/create_guestlog_entry_response.html'
    permission_required = (
        'desklogs.change_guestlogentry'
    )

    def get(self, request):
        guestlog_pk = request.GET.get('guestlog_pk')
        guestlog = GuestLog.objects.get(pk=guestlog_pk)

        entry_pk = request.GET.get('current_entry_being_updated_pk')
        host_name = request.GET.get('host_name')
        guest_name = request.GET.get('guest_name')
        entry = GuestLogEntry.objects.get(pk=entry_pk)
        entry.host_name = host_name
        entry.guest_name = guest_name
        entry.completed = True
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


class CheckoutGuestlogEntry(LoginRequiredMixin, PermissionRequiredMixin, View):
    template_name = 'desklogs/create_guestlog_entry_response.html'
    permission_required = (
        'desklogs.change_guestlogentry'
    )

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


class FilterGuestlogEntries(LoginRequiredMixin, PermissionRequiredMixin, View):
    template_name = 'desklogs/create_guestlog_entry_response.html'
    permission_required = (
        'desklogs.view_guestlogentry'
    )

    def get(self, request):
        query = request.GET.get('query')
        guestlog_pk = request.GET.get('guestlog_pk')
        guestlog = GuestLog.objects.get(pk=guestlog_pk)
        entries = guestlog.guestlogentry_set.filter(Q(host_name__contains=query) | Q(guest_name__contains=query))
        checked_in_entries = entries.filter(guest_checked_in=True)
        checked_out_entries = entries.filter(guest_checked_in=False)

        user = self.request.user
        disable = False
        for entry in user.guestlog.guestlogentry_set.all():
            if entry.host_name is None or entry.guest_name is None:
                disable = True

        context = {
            'user': self.request.user, 'guestlog': guestlog,
            'guestlog_entries': checked_in_entries | checked_out_entries,
            'disable_creation': True if disable else False
        }

        return render(request, self.template_name, context)


class EquipmentLogEntryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = EquipmentLogEntry
    template_name = 'desklogs/equipmentlog.html'
    permission_required = (
        'desklogs.view_equipmentlog', 'desklogs.add_equipmentlogentry'
    )

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = self.request.user
        context['user'] = user
        context['equipmentlog'] = user.equipmentlog
        checked_in_list = user.equipmentlog.equipmentlogentry_set.filter(completed=True)
        checked_out_list = user.equipmentlog.equipmentlogentry_set.filter(completed=False)
        context['equipmentlog_entries'] = checked_out_list | checked_in_list
        for entry in user.equipmentlog.equipmentlogentry_set.all():
            if not entry.item_host:
                context['disable_creation'] = True
        return context


class CreateBlankEquipmentLogEntry(LoginRequiredMixin, PermissionRequiredMixin, View):
    template_name = 'desklogs/create_equipmentlog_entry_response.html'
    permission_required = (
        'desklogs.add_equipmentlogentry'
    )

    def get(self, request):
        equipmentlog_pk = request.GET.get('equipmentlog_pk')
        equipmentlog = EquipmentLog.objects.get(pk=equipmentlog_pk)
        now = datetime.datetime.now()
        time = '{0}:{1}:{2}'.format(str(now.hour),
                                    '0' + str(now.minute) if len(str(now.minute)) == 1 else str(now.minute),
                                    '0' + str(now.second) if len(str(now.second)) == 1 else str(now.second))
        date = '{0}-{1}-{2}'.format(str(now.month), str(now.day), str(now.year))
        EquipmentLogEntry.objects.create(equipment_log=equipmentlog, time_out=time, date_out=date)

        user = self.request.user
        disable = False
        for entry in user.equipmentlog.equipmentlogentry_set.all():
            if entry.item_host is None:
                disable = True

        checked_in_list = user.equipmentlog.equipmentlogentry_set.filter(completed=True)
        checked_out_list = user.equipmentlog.equipmentlogentry_set.filter(completed=False)

        context = {
            'user': self.request.user, 'equipmentlog': equipmentlog,
            'equipmentlog_entries': checked_out_list | checked_in_list,
            'disable_creation': True if disable else False
        }
        return render(request, self.template_name, context)


class UpdateEquipmentlogEntry(LoginRequiredMixin, PermissionRequiredMixin, View):
    template_name = 'desklogs/create_equipmentlog_entry_response.html'
    permission_required = (
        'desklogs.change_equipmentlogentry'
    )

    def get(self, request):
        equipmentlog_pk = request.GET.get('equipmentlog_pk')
        equipmentlog = EquipmentLog.objects.get(pk=equipmentlog_pk)

        entry_pk = request.GET.get('current_entry_being_updated_pk')
        item_host = request.GET.get('item_host')
        initial_condition = request.GET.get('initial_condition')
        item = request.GET.get('item')
        entry = EquipmentLogEntry.objects.get(pk=entry_pk)
        entry.item_host = item_host
        entry.item_checked_out = True
        entry.initial_condition = initial_condition
        entry.item = item
        entry.save()

        user = self.request.user
        disable = False
        for entry in user.equipmentlog.equipmentlogentry_set.all():
            if entry.item_host is None:
                disable = True

        checked_in_list = user.equipmentlog.equipmentlogentry_set.filter(completed=True)
        checked_out_list = user.equipmentlog.equipmentlogentry_set.filter(completed=False)

        context = {
            'user': self.request.user, 'equipmentlog': equipmentlog,
            'equipmentlog_entries': checked_out_list | checked_in_list,
            'disable_creation': True if disable else False
        }
        return render(request, self.template_name, context)


class CheckinEquipmentlogEntry(LoginRequiredMixin, PermissionRequiredMixin, View):
    template_name = 'desklogs/create_equipmentlog_entry_response.html'
    permission_required = (
        'desklogs.change_equipmentlogentry'
    )

    def get(self, request):
        equipmentlog_pk = request.GET.get('equipmentlog_pk')
        equipmentlog = EquipmentLog.objects.get(pk=equipmentlog_pk)
        entry_pk = request.GET.get('current_entry_being_updated_pk')
        entry = EquipmentLogEntry.objects.get(pk=entry_pk)
        entry.completed = True
        entry.item_checked_out = False
        entry.final_condition = request.GET.get('final_condition')
        now = datetime.datetime.now()
        time = '{0}:{1}:{2}'.format(str(now.hour),
                                    '0' + str(now.minute) if len(str(now.minute)) == 1 else str(now.minute),
                                    '0' + str(now.second) if len(str(now.second)) == 1 else str(now.second))
        date = '{0}-{1}-{2}'.format(str(now.month), str(now.day), str(now.year))
        entry.time_in = time
        entry.date_in = date
        entry.save()
        user = self.request.user
        disable = False
        for entry in user.equipmentlog.equipmentlogentry_set.all():
            if entry.item_host is None:
                disable = True

        checked_in_list = user.equipmentlog.equipmentlogentry_set.filter(completed=True)
        checked_out_list = user.equipmentlog.equipmentlogentry_set.filter(completed=False)

        context = {
            'user': self.request.user, 'equipmentlog': equipmentlog,
            'equipmentlog_entries': checked_out_list | checked_in_list,
            'disable_creation': True if disable else False
        }
        return render(request, self.template_name, context)


class FilterEquipmentLogEntries(LoginRequiredMixin, PermissionRequiredMixin, View):
    template_name = 'desklogs/create_equipmentlog_entry_response.html'
    permission_required = (
        'desklogs.view_equipmentlogentry'
    )

    def get(self, request):
        equipmentlog_pk = request.GET.get('equipmentlog_pk')
        equipmentlog = EquipmentLog.objects.get(pk=equipmentlog_pk)
        query = request.GET.get('query')

        entries = equipmentlog.equipmentlogentry_set.filter(Q(item_host__contains=query) | Q(item__contains=query))
        completed_entries = entries.filter(completed=True)
        not_completed_entries = entries.filter(completed=False)

        user = self.request.user
        disable = False
        for entry in user.equipmentlog.equipmentlogentry_set.all():
            if entry.item_host is None:
                disable = True

        context = {
            'user': self.request.user, 'equipmentlog': equipmentlog,
            'equipmentlog_entries': not_completed_entries | completed_entries,
            'disable_creation': True if disable else False
        }
        return render(request, self.template_name, context)


class LockoutLogEntryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = LockoutLogEntry
    template_name = 'desklogs/lockoutlog.html'
    permission_required = (
        'desklogs.view_lockoutlog', 'desklogs.view_lockoutlogentry'
    )

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = self.request.user
        context['lockoutlog'] = user.lockoutlog
        context['lockoutlog_entries'] = user.lockoutlog.lockoutlogentry_set.all().order_by('user__student_id')

        return context


class FilterLockoutLogEntries(LoginRequiredMixin, PermissionRequiredMixin, View):
    template_name = 'desklogs/lockoutlog_response.html'
    permission_required = (
        'desklogs.view_lockoutlogentry'
    )

    def get(self, request):
        lockoutlog_pk = request.GET.get('lockoutlog_pk')
        lockoutlog = LockoutLog.objects.get(pk=lockoutlog_pk)
        query = request.GET.get('query')

        entries = lockoutlog.lockoutlogentry_set.filter(user__email__contains=query).order_by('user__student_id')

        context = {
            'lockoutlog': lockoutlog,
            'lockoutlog_entries': entries,
        }
        return render(request, self.template_name, context)


class LockoutLogEntryHistory(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = LockoutLogEntry
    template_name = 'desklogs/lockoutlog_entry_history.html'
    permission_required = (
        'desklogs.view_lockoutcode'
    )


class CreateLockoutCodeTimeAndDate(LoginRequiredMixin, PermissionRequiredMixin, View):
    template_name = 'desklogs/lockoutlog_entry_history_response.html'
    permission_required = (
        'desklogs.add_lockoutcode'
    )

    def get(self, request):
        entry = request.GET.get('lockoutlog_entry_pk')
        lockoutlog_entry = LockoutLogEntry.objects.get(pk=entry)
        now = datetime.datetime.now()
        time = '{0}:{1}:{2}'.format(str(now.hour),
                                    '0' + str(now.minute) if len(str(now.minute)) == 1 else str(now.minute),
                                    '0' + str(now.second) if len(str(now.second)) == 1 else str(now.second))
        date = '{0}-{1}-{2}'.format(str(now.month), str(now.day), str(now.year))
        LockoutCode.objects.create(lockout_log_entry=lockoutlog_entry, date_code_given=date, time_code_given=time)

        context = {
            'lockoutlogentry': lockoutlog_entry
        }
        return render(request, self.template_name, context)


class PassDownLogEntryListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'desklogs/passdownlog.html'
    model = PassDownLogEntry
    permission_required = (
        'desklogs.view_passdownlog', 'desklogs.view_passdownlogentry'
    )

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = self.request.user
        context['passdown_log'] = user.passdownlog
        context['passdown_log_entries'] = user.passdownlog.passdownlogentry_set.all().order_by('-time')
        for entry in user.passdownlog.passdownlogentry_set.all():
            if not entry.initials:
                context['disable_creation'] = True
        return context


class CreateBlankPassDownLogEntry(LoginRequiredMixin, PermissionRequiredMixin, View):
    template_name = 'desklogs/passdownlog_response.html'
    permission_required = (
        'desklogs.add_passdownlogentry'
    )

    def get(self, request):
        passdownlog_pk = request.GET.get('passdownlog_pk')
        passdownlog = PassDownLog.objects.get(pk=passdownlog_pk)
        now = datetime.datetime.now()
        time = '{0}:{1}:{2}'.format(str(now.hour),
                                    '0' + str(now.minute) if len(str(now.minute)) == 1 else str(now.minute),
                                    '0' + str(now.second) if len(str(now.second)) == 1 else str(now.second))
        date = '{0}-{1}-{2}'.format(str(now.month), str(now.day), str(now.year))
        PassDownLogEntry.objects.create(passdown_log=passdownlog, time=time, date=date)

        user = self.request.user
        disable = False
        for entry in user.passdownlog.passdownlogentry_set.all():
            if not entry.message:
                disable = True

        context = {
            'passdown_log': passdownlog,
            'passdown_log_entries': passdownlog.passdownlogentry_set.all().order_by('-time'),
            'disable_creation': True if disable else False
        }
        return render(request, self.template_name, context)


class UpdatePassDownLogEntry(LoginRequiredMixin, PermissionRequiredMixin, View):
    template_name = 'desklogs/passdownlog_response.html'
    permission_required = (
        'desklogs.change_passdownlogentry'
    )

    def get(self, request):
        passdownlog_pk = request.GET.get('passdownlog_pk')
        passdownlog = PassDownLog.objects.get(pk=passdownlog_pk)
        passdownlog_entry_pk = request.GET.get('current_entry_being_updated_pk')
        message = request.GET.get('message')
        initials = request.GET.get('initials')
        entry = PassDownLogEntry.objects.get(pk=passdownlog_entry_pk)
        entry.message = message
        entry.initials = initials
        entry.completed = True
        entry.save()

        user = self.request.user
        disable = False
        for entry in user.passdownlog.passdownlogentry_set.all():
            if not entry.message:
                disable = True

        context = {
            'passdown_log': passdownlog,
            'passdown_log_entries': passdownlog.passdownlogentry_set.all().order_by('-time'),
            'disable_creation': True if disable else False
        }
        return render(request, self.template_name, context)


class FilterPassDownLogEntries(LoginRequiredMixin, PermissionRequiredMixin, View):
    template_name = 'desklogs/passdownlog_response.html'
    permission_required = (
        'desklogs.view_passdownlogentry'
    )

    def get(self, request):
        query = request.GET.get('query')
        passdownlog_pk = request.GET.get('passdown_log')
        passdownlog = PassDownLog.objects.get(pk=passdownlog_pk)
        entries = passdownlog.passdownlogentry_set.filter(Q(message__contains=query) | Q(initials__contains=query))

        user = self.request.user
        disable = False
        for entry in user.passdownlog.passdownlogentry_set.all():
            if not entry.message:
                disable = True

        context = {
            'passdown_log': passdownlog,
            'passdown_log_entries': entries.order_by('-time'),
            'disable_creation': True if disable else False
        }
        return render(request, self.template_name, context)
