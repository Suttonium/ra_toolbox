from django.db import models

# Create your models here.
from accounts.models import User
from django.utils.translation import ugettext_lazy as _
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
    condition = models.IntegerField(choices=DAMAGE_CHOICES, null=True)

    def __str__(self):
        return 'Equipment Log Entry for Equipment Log at {0}'.format(self.equipment_log.user.email)

    class Meta:
        verbose_name = _('Equipment Log Entry')
        verbose_name_plural = _('Equipment Log Entries')
