from django.forms import ModelForm
from django import forms
from informationcards.models import StudentInformationCard
from django.utils.translation import ugettext_lazy as _
from .constants import *


class StudentInformationCardPartOneForm(ModelForm):
    class Meta:
        model = StudentInformationCard
        fields = ['date_of_birth', 'cell_phone_number', 'home_street_address', 'home_city',
                  'home_state', 'zip_code']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('First Name')}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Last Name')}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cell_phone_number': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': _('Phone Number'), 'maxlength': PHONE_NUMBER_MAX_LIMIT}),
            'home_street_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Street')}),
            'home_city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('City')}),
            'home_state': forms.Select(attrs={'class': 'form-control'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Zip Code')}),
            # 'allergies': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Allergies')})
        }


class StudentInformationCardPartTwoForm(ModelForm):
    class Meta:
        model = StudentInformationCard
        fields = ['allergies', 'medications_or_special_needs', 'physical_assistance']
        widgets = {
            'allergies': forms.Textarea(attrs={'class': 'form-control', 'placeholder': ALLERGIES, 'id': 'allergies'}),
            'medications_or_special_needs': forms.Textarea(attrs={'class': 'form-control', 'placeholder': MEDICATIONS,
                                                                  'id': 'medications_or_special_needs'}),
            'physical_assistance': forms.CheckboxInput(attrs={'class': 'form-control', 'id': 'physical_assistance'})
        }
