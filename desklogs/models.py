# Create your models here.
from django.utils.translation import ugettext_lazy as _

from accounts.models import User, Student
from residencehalls.models import *
from .constants import *


class GuestLog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Guest Log for {0}'.format(self.user.email)

    class Meta:
        verbose_name = _('Guest Log')
        verbose_name_plural = _('Guest Logs')


class GuestLogEntry(models.Model):
    guest_log = models.ForeignKey(GuestLog, on_delete=models.CASCADE)
    time_in = models.CharField(max_length=100, null=True, blank=True)
    time_out = models.CharField(max_length=100, null=True, blank=True)
    date_in = models.CharField(max_length=100, null=True, blank=True)
    date_out = models.CharField(max_length=100, null=True, blank=True)
    host_name = models.CharField(max_length=100, null=True)
    guest_name = models.CharField(max_length=100, null=True)
    physical_assistance_required = models.BooleanField(default=False)
    guest_checked_in = models.BooleanField(default=True)
    overnight = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return 'Guest Log Entry for the Guest Log at {0}'.format(self.guest_log.user.email)

    class Meta:
        verbose_name = _('Guest Log Entry')
        verbose_name_plural = _('Guest Log Entries')


class EquipmentLog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Equipment Log for {0}'.format(self.user.email)

    class Meta:
        verbose_name = _('Equipment Log')
        verbose_name_plural = _('Equipment Logs')


class EquipmentLogEntry(models.Model):
    equipment_log = models.ForeignKey(EquipmentLog, on_delete=models.CASCADE)
    time_out = models.CharField(max_length=100, null=True, blank=True)
    date_out = models.CharField(max_length=100, null=True, blank=True)
    time_in = models.CharField(max_length=100, null=True, blank=True)
    date_in = models.CharField(max_length=100, null=True, blank=True)
    item_host = models.CharField(max_length=100, null=True)
    item = models.CharField(max_length=100, null=True)
    initial_condition = models.IntegerField(choices=DAMAGE_CHOICES, null=True)
    final_condition = models.IntegerField(choices=DAMAGE_CHOICES, null=True)
    item_checked_out = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return 'Equipment Log Entry for Equipment Log at {0}'.format(self.equipment_log.user.email)

    class Meta:
        verbose_name = _('Equipment Log Entry')
        verbose_name_plural = _('Equipment Log Entries')


class LockoutLog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    residence_hall = models.OneToOneField(ResidenceHall, on_delete=models.CASCADE, null=True)
    east_campus_lockout_log = models.BooleanField(default=False)

    def __str__(self):
        return 'Lockout Log for {0}'.format(self.user.email)

    class Meta:
        verbose_name = _('Lockout Log')
        verbose_name_plural = _('Lockout Logs')


class LockoutLogEntry(models.Model):
    lockout_log = models.ForeignKey(LockoutLog, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Lockout Log Entry for {0}'.format(self.user.email)

    class Meta:
        verbose_name = _('Lockout Log Entry')
        verbose_name_plural = _('Lockout Log Entries')


class LockoutCode(models.Model):
    lockout_log_entry = models.ForeignKey(LockoutLogEntry, on_delete=models.CASCADE)
    date_code_given = models.CharField(max_length=100, null=True, blank=True)
    time_code_given = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return 'Lockout Code for {0}'.format(self.lockout_log_entry.user.email)

    class Meta:
        verbose_name = _('Lockout Code')
        verbose_name_plural = _('Lockout Codes')


class PassDownLog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Pass Down for {0}'.format(self.user.email)

    class Meta:
        verbose_name = _('Pass Down Log')
        verbose_name_plural = _('Pass Down Logs')


class PassDownLogEntry(models.Model):
    passdown_log = models.ForeignKey(PassDownLog, on_delete=models.CASCADE)
    time = models.CharField(max_length=100, null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField()
    initials = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return 'Pass Down Log Entry for Pass Down Log at {0}'.format(self.passdown_log.user.email)

    class Meta:
        verbose_name = _('Pass Down Log Entry')
        verbose_name_plural = _('Pass Down Log Entries')
