from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from informationcards.models import StudentInformationCard
from .constants import *
from .functions import *


class StudentInformationCardPartOneForm(ModelForm):
    def clean_date_of_birth(self):
        dob = self.cleaned_data['date_of_birth']
        if in_the_future(dob):
            raise ValidationError(
                _('This date is a future date. Please enter a previous date or the current date.'))
        return dob

    class Meta:
        model = StudentInformationCard
        fields = ['date_of_birth', 'cell_phone_number', 'home_street_address', 'home_city',
                  'home_state', 'zip_code']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cell_phone_number': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': CELL_PHONE_NUMBER,
                       'maxlength': PHONE_NUMBER_MAX_LIMIT}),
            'home_street_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': STREET}),
            'home_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': CITY}),
            'home_state': forms.Select(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ZIP_CODE}),
        }


class StudentInformationCardPartTwoForm(ModelForm):
    class Meta:
        model = StudentInformationCard
        fields = ['allergies', 'medications_or_special_needs', 'physical_assistance']
        widgets = {
            'allergies': forms.Textarea(attrs={'class': 'form-control', 'placeholder': ALLERGIES, 'id': 'allergies'}),
            'medications_or_special_needs': forms.Textarea(attrs={'class': 'form-control', 'placeholder': MEDICATIONS,
                                                                  'id': 'medications_or_special_needs'}),
            'physical_assistance': forms.Textarea(
                attrs={'class': 'form-control', 'id': 'physical_assistance', 'placeholder': PHYSICAL_ASSISTANCE})
        }


class StudentInformationCardPartThreeForm(ModelForm):
    class Meta:
        model = StudentInformationCard
        fields = ['emergency_contact_one_name', 'emergency_contact_one_relationship_to_student',
                  'emergency_contact_one_primary_phone_number', 'emergency_contact_two_name',
                  'emergency_contact_two_relationship_to_student', 'emergency_contact_two_primary_phone_number',
                  'emergency_contact_three_name', 'emergency_contact_three_relationship_to_student',
                  'emergency_contact_three_primary_phone_number']
        widgets = {
            'emergency_contact_one_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'emergency_contact_one_name',
                       'placeholder': EMERGENCY_CONTACT_NAME}),
            'emergency_contact_one_relationship_to_student': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'emergency_contact_one_relationship_to_student',
                       'placeholder': EMERGENCY_CONTACT_RELATIONSHIP_TO_STUDENT}),
            'emergency_contact_one_primary_phone_number': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'emergency_contact_one_primary_phone_number',
                       'placeholder': EMERGENCY_CONTACT_PRIMARY_PHONE_NUMBER}),
            'emergency_contact_two_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'emergency_contact_two_name',
                       'placeholder': EMERGENCY_CONTACT_NAME}),
            'emergency_contact_two_relationship_to_student': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'emergency_contact_two_relationship_to_student',
                       'placeholder': EMERGENCY_CONTACT_RELATIONSHIP_TO_STUDENT}),
            'emergency_contact_two_primary_phone_number': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'emergency_contact_two_primary_phone_number',
                       'placeholder': EMERGENCY_CONTACT_PRIMARY_PHONE_NUMBER}),
            'emergency_contact_three_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'emergency_contact_three_name',
                       'placeholder': EMERGENCY_CONTACT_NAME}),
            'emergency_contact_three_relationship_to_student': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'emergency_contact_three_relationship_to_student',
                       'placeholder': EMERGENCY_CONTACT_RELATIONSHIP_TO_STUDENT}),
            'emergency_contact_three_primary_phone_number': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'emergency_contact_three_primary_phone_number',
                       'placeholder': EMERGENCY_CONTACT_PRIMARY_PHONE_NUMBER})
        }


class EntireStudentInformationCardForm(ModelForm):
    def clean_date_of_birth(self):
        dob = self.cleaned_data['date_of_birth']
        if in_the_future(dob):
            raise ValidationError(
                _('This date is a future date. Please enter a previous date or the current date.'))
        return dob

    class Meta:
        model = StudentInformationCard
        exclude = ('user',)
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cell_phone_number': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': CELL_PHONE_NUMBER,
                       'maxlength': PHONE_NUMBER_MAX_LIMIT}),
            'home_street_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': STREET}),
            'home_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': CITY}),
            'home_state': forms.Select(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ZIP_CODE}),
            'allergies': forms.Textarea(attrs={'class': 'form-control', 'placeholder': ALLERGIES, 'id': 'allergies'}),
            'medications_or_special_needs': forms.Textarea(attrs={'class': 'form-control', 'placeholder': MEDICATIONS,
                                                                  'id': 'medications_or_special_needs'}),
            'physical_assistance': forms.Textarea(
                attrs={'class': 'form-control', 'id': 'physical_assistance', 'placeholder': PHYSICAL_ASSISTANCE}),
            'emergency_contact_one_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'emergency_contact_one_name',
                       'placeholder': EMERGENCY_CONTACT_NAME}),
            'emergency_contact_one_relationship_to_student': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'emergency_contact_one_relationship_to_student',
                       'placeholder': EMERGENCY_CONTACT_RELATIONSHIP_TO_STUDENT}),
            'emergency_contact_one_primary_phone_number': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'emergency_contact_one_primary_phone_number',
                       'placeholder': EMERGENCY_CONTACT_PRIMARY_PHONE_NUMBER}),
            'emergency_contact_two_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'emergency_contact_two_name',
                       'placeholder': EMERGENCY_CONTACT_NAME}),
            'emergency_contact_two_relationship_to_student': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'emergency_contact_two_relationship_to_student',
                       'placeholder': EMERGENCY_CONTACT_RELATIONSHIP_TO_STUDENT}),
            'emergency_contact_two_primary_phone_number': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'emergency_contact_two_primary_phone_number',
                       'placeholder': EMERGENCY_CONTACT_PRIMARY_PHONE_NUMBER}),
            'emergency_contact_three_name': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'emergency_contact_three_name',
                       'placeholder': EMERGENCY_CONTACT_NAME}),
            'emergency_contact_three_relationship_to_student': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'emergency_contact_three_relationship_to_student',
                       'placeholder': EMERGENCY_CONTACT_RELATIONSHIP_TO_STUDENT}),
            'emergency_contact_three_primary_phone_number': forms.TextInput(
                attrs={'class': 'form-control', 'id': 'emergency_contact_three_primary_phone_number',
                       'placeholder': EMERGENCY_CONTACT_PRIMARY_PHONE_NUMBER})
        }
