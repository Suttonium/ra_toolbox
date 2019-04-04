from django import forms
from django.forms import ModelForm

from trackers.models import Tracker


class TrackerForm(ModelForm):
    class Meta:
        model = Tracker
        fields = ['general_information', 'knock_and_talk_one_information', 'knock_and_talk_two_information',
                  'knock_and_talk_three_information']
        widgets = {
            'general_information': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'General Information About the Resident'}),
            'knock_and_talk_one_information': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Knock and Talk #1 Information'}),
            'knock_and_talk_two_information': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Knock and Talk #2 Information'}),
            'knock_and_talk_three_information': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Knock and Talk #3 Information'})
        }
