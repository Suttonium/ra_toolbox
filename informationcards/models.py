from django.core.validators import MinLengthValidator
from django.db import models
from .constants import *
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class StudentInformationCard(models.Model):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE)
    date_of_birth = models.CharField(_('date of birth'), default='', max_length=MAX_DATE_LENGTH, null=True)
    cell_phone_number = models.CharField(_('cell phone number'), unique=True, max_length=PHONE_NUMBER_MAX_LIMIT,
                                         validators=[MinLengthValidator(PHONE_NUMBER_MIN_LIMIT)], null=True)
    home_street_address = models.CharField(_('home street address'), max_length=ADDRESS_MAX_LIMIT, default='',
                                           null=True)
    home_city = models.CharField(_('home city'), max_length=ADDRESS_MAX_LIMIT, default='', null=True)
    home_state = models.CharField(_('home state'), max_length=STATE_LENGTH, default='', null=True,
                                  choices=STATE_ABBREVIATIONS)
    zip_code = models.IntegerField(_('zip code'), null=True)
    allergies = models.TextField(_('allergies'), default='', null=True)
    physical_assistance = models.TextField(_('physical_assistance'), default='', null=True)
    medications_or_special_needs = models.TextField(_('medications or special needs'), default='', null=True)

    emergency_contact_one_name = models.CharField(_('name of emergency contact one'), max_length=EC_NAME_LENGTH,
                                                  default='', null=True)
    emergency_contact_one_relationship_to_student = models.CharField(
        _('relationship of emergency contact one to student'), max_length=EC_RELATIONSHIP_TO_STUDENT_LENGTH,
        default='', null=True)
    emergency_contact_one_primary_phone_number = models.CharField(_('primary phone number of emergency contact one'),
                                                                  max_length=PHONE_NUMBER_MAX_LIMIT,
                                                                  validators=[
                                                                      MinLengthValidator(PHONE_NUMBER_MIN_LIMIT)],
                                                                  default='', null=True)
    emergency_contact_two_name = models.CharField(_('name of emergency contact two'), max_length=EC_NAME_LENGTH,
                                                  default='', null=True)
    emergency_contact_two_relationship_to_student = models.CharField(
        _('relationship of emergency contact two to student'), max_length=EC_RELATIONSHIP_TO_STUDENT_LENGTH,
        default='', null=True)
    emergency_contact_two_primary_phone_number = models.CharField(_('primary phone number of emergency contact two'),
                                                                  max_length=PHONE_NUMBER_MAX_LIMIT,
                                                                  validators=[
                                                                      MinLengthValidator(PHONE_NUMBER_MIN_LIMIT)],
                                                                  default='', null=True)
    emergency_contact_three_name = models.CharField(_('name of emergency contact three'), max_length=EC_NAME_LENGTH,
                                                    default='', null=True)
    emergency_contact_three_relationship_to_student = models.CharField(
        _('relationship of emergency contact three to student'), max_length=EC_RELATIONSHIP_TO_STUDENT_LENGTH,
        default='', null=True)
    emergency_contact_three_primary_phone_number = models.CharField(
        _('primary phone number of emergency contact three'),
        max_length=PHONE_NUMBER_MAX_LIMIT,
        validators=[
            MinLengthValidator(PHONE_NUMBER_MIN_LIMIT)],
        default='', null=True)

    def __str__(self):
        return 'Student Information Card for {0}'.format(self.user.email)

    class Meta:
        verbose_name = _('Student Information Card')
        verbose_name_plural = _('Student Information Cards')
