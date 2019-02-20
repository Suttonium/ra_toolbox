from django.core.validators import MinLengthValidator
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager
from .constants import *


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=NAME_LIMIT, blank=True)
    middle_name = models.CharField(_('middle name'), max_length=NAME_LIMIT, blank=True)
    last_name = models.CharField(_('last name'), max_length=NAME_LIMIT, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    student_id = models.CharField(_('student id'), unique=True, max_length=STUDENT_ID_MAX_LIMIT,
                                  validators=[MinLengthValidator(STUDENT_ID_MIN_LIMIT)])
    is_resident_assistant = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_hall_director = models.BooleanField(default=False)
    is_desk_account = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return '{0}'.format(self.email)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roommates = models.ManyToManyField('self', blank=True)
    suitemates = models.ManyToManyField('self', blank=True)
    resident_assistant = models.ForeignKey('ResidentAssistant', on_delete=models.CASCADE)
    residence_hall = models.ForeignKey('residencehalls.ResidenceHall', on_delete=models.CASCADE)
    suite = models.ForeignKey('residencehalls.Suite', on_delete=models.CASCADE, null=True)
    hallway = models.ForeignKey('residencehalls.Hallway', on_delete=models.CASCADE, null=True)
    room = models.ForeignKey('residencehalls.Room', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{0}'.format(self.user.email)

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')


class ResidentAssistant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    activation_code = models.CharField(max_length=ACTIVATION_CODE_LIMIT, default='')
    residence_hall = models.ForeignKey('residencehalls.ResidenceHall', on_delete=models.CASCADE)
    suite = models.ForeignKey('residencehalls.Suite', on_delete=models.CASCADE, null=True)
    room = models.ForeignKey('residencehalls.Room', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{0}'.format(self.user.email)

    class Meta:
        verbose_name = _('Resident Assistant')
        verbose_name_plural = _('Resident Assistants')


class HallDirector(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{0}'.format(self.user.email)

    class Meta:
        verbose_name_plural = _('Hall Directors')
        verbose_name = _('Hall Director')
