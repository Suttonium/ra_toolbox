from django.contrib.auth.models import Group

from informationcards.models import StudentInformationCard
from trackers.models import Tracker
from .models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def add_user_to_proper_group(sender, instance, created, **kwargs):
    if created:
        if instance.is_resident_assistant:
            Group.objects.get(name='Resident Assistant Group').user_set.add(instance)
            StudentInformationCard.objects.create(user=instance)
        if instance.is_student:
            Group.objects.get(name='Student Group').user_set.add(instance)
            StudentInformationCard.objects.create(user=instance)
            Tracker.objects.create(user=instance)
            instance.save()
        if instance.is_hall_director:
            Group.objects.get(name='Hall Director Group').user_set.add(instance)
        if instance.is_desk_account:
            Group.objects.get(name='Desk Account Group').user_set.add(instance)
