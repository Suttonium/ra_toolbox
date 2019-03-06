from django.db import models
from accounts.models import ResidentAssistant, HallDirector
from django.utils.translation import ugettext_lazy as _


# Create your models here.


class ResidenceHall(models.Model):
    name = models.CharField(max_length=256, unique=True)
    hall_director = models.ForeignKey(HallDirector, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = _('Residence Hall')
        verbose_name_plural = _('Residence Halls')

    def __str__(self):
        return self.name


class Suite(models.Model):
    number = models.IntegerField()
    hallway = models.ForeignKey('Hallway', on_delete=models.CASCADE)
    residence_hall = models.ForeignKey(ResidenceHall, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = _('Suite')
        verbose_name_plural = _('Suites')

    def __str__(self):
        return "{0} Suite #{1}".format(self.hallway.residence_hall.name, self.number)


class Room(models.Model):
    suite = models.ForeignKey(Suite, on_delete=models.CASCADE, null=True)
    letter = models.CharField(max_length=1)
    residence_hall = models.ForeignKey(ResidenceHall, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = _('Room')
        verbose_name_plural = _('Rooms')

    def __str__(self):
        return "{0}{1}".format(self.suite, self.letter)


class Hallway(models.Model):
    floor = models.CharField(max_length=2)
    residence_hall = models.ForeignKey(ResidenceHall, on_delete=models.CASCADE)
    resident_assistant = models.OneToOneField(ResidentAssistant, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{0} Floor {1}".format(self.residence_hall.name, self.floor)

    class Meta:
        verbose_name = _('Hallway')
        verbose_name_plural = _('Hallways')
