from django.db import models

# Create your models here.
from accounts.models import User
from django.utils.translation import ugettext_lazy as _


class GuestLog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Guest Log for {0}'.format(self.user.email)

    class Meta:
        verbose_name = _('Guest Log')


class GuestLogEntry(models.Model):
    guest_log = models.ForeignKey(GuestLog, on_delete=models.CASCADE)

    def __str__(self):
        return 'Guest Log Entry for the Guest Log at {0}'.format(self.guest_log.user.email)

    class Meta:
        verbose_name = _('Guest Log Entry')
        verbose_name_plural = _('Guest Log Entries')
