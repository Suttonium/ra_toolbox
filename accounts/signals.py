from django.contrib.auth.models import Group

from desklogs.models import *
from informationcards.models import StudentInformationCard
from trackers.models import Tracker
from .models import User, Student, DeskAccount
from django.db.models.signals import post_save
from django.dispatch import receiver
from securityquestions.models import *
from residencehalls.constants import *


@receiver(post_save, sender=User)
def add_user_to_proper_group(sender, instance, created, **kwargs):
    if created:
        if instance.is_resident_assistant:
            Group.objects.get(name='Resident Assistant Group').user_set.add(instance)
            StudentInformationCard.objects.create(user=instance)
            SecurityQuestions.objects.create(user=instance)
        if instance.is_student:
            Group.objects.get(name='Student Group').user_set.add(instance)
            StudentInformationCard.objects.create(user=instance)
            Tracker.objects.create(user=instance)
            SecurityQuestions.objects.create(user=instance)
        if instance.is_hall_director:
            Group.objects.get(name='Hall Director Group').user_set.add(instance)
        if instance.is_desk_account:
            Group.objects.get(name='Desk Account Group').user_set.add(instance)
            GuestLog.objects.create(user=instance)
            EquipmentLog.objects.create(user=instance)
            PassDownLog.objects.create(user=instance)


@receiver(post_save, sender=DeskAccount)
def add_lockout_log_to_desk_account(sender, instance, created, **kwargs):
    if created:
        if instance.residence_hall:
            LockoutLog.objects.create(user=instance.user, residence_hall=instance.residence_hall)
        else:
            LockoutLog.objects.create(user=instance.user, east_campus_lockout_log=True)


@receiver(post_save, sender=Student)
def add_lockout_log_entry_to_student(sender, instance, created, **kwargs):
    if created:
        if instance.residence_hall.name not in east_campus_list:
            LockoutLogEntry.objects.create(user=instance.user,
                                           lockout_log=LockoutLog.objects.get(residence_hall=instance.residence_hall))
        else:
            LockoutLogEntry.objects.create(user=instance.user,
                                           lockout_log=LockoutLog.objects.get(east_campus_lockout_log=True))


@receiver(post_save, sender=ResidentAssistant)
def add_lockout_log_entry_to_resident_assistant(sender, instance, created, **kwargs):
    if created:
        if instance.residence_hall.name not in east_campus_list:
            LockoutLogEntry.objects.create(user=instance.user,
                                           lockout_log=LockoutLog.objects.get(residence_hall=instance.residence_hall))
        else:
            LockoutLogEntry.objects.create(user=instance.user,
                                           lockout_log=LockoutLog.objects.get(east_campus_lockout_log=True))
