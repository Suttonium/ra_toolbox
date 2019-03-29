from django.forms import ModelForm
from django import forms
from .models import *


class SecurityQuestionsForm(ModelForm):
    class Meta:
        model = SecurityQuestions
        widgets = {
            'favorite_color': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Favorite Color', 'id': 'favorite_color'}),
            'high_school': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'High School', 'id': 'high_school'}),
            'birth_city': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Birth City', 'id': 'birth_city'}),
            'favorite_social_media_platform': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Favorite Social Media Platform',
                       'id': 'favorite_social_media_platform'}),
            'road': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Road', 'id': 'road'}),
            'favorite_food': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Favorite Food', 'id': 'favorite_food'})
        }
