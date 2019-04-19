from django import forms
from django.forms import ModelForm

from .models import *


class FeedbackSubmissionForm(ModelForm):
    class Meta:
        model = FeedbackSubmission
        fields = '__all__'
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Email Address'}),
            'text': forms.Textarea(
                attrs={'class': 'form-control', 'id': 'text_input', 'placeholder': 'Enter Feedback Here'})
        }
