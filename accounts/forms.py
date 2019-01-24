from django import forms
from django.core.exceptions import ValidationError

from django.forms import ModelForm
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from django.utils.translation import ugettext_lazy as _

from accounts.tokens import account_activation_token
from .models import User, Student, ResidentAssistant
from .constants import ACTIVATION_CODE_LIMIT, ATCNUEDU
# from .functions import send_email
from residencehalls.models import ResidenceHall, Hallway
from django.utils.crypto import get_random_string
from django.contrib.sites.models import Site
from django.core.mail import send_mail
from capstone import settings


class StudentRegistrationForm(ModelForm):
    code_for_assigning_ra = forms.CharField(required=True, max_length=ACTIVATION_CODE_LIMIT, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'id_code_for_assigning_ra', 'placeholder': _('Activation Code')}))
    password_confirmation = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': _('Password Confirmation'), 'id': 'id_password_confirmation'}))

    def save(self, commit=True, **kwargs):
        user = super().save(commit=False)
        user.is_student = True
        user.set_password(user.password)
        # user.first_name, user.last_name = get_names(self.cleaned_data.get('email'))
        if commit:
            user.save()
            mail_subject = 'Attempted Student Registration'
            current_email = self.cleaned_data.get('email')
            plain_text_message = render_to_string('emails/student_signup_email.html', {
                'domain': Site.objects.get_current(),
                'email': current_email,
                'uidb64': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            send_mail(subject=mail_subject,
                      message=plain_text_message,
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[current_email])
        resident_assistant = ResidentAssistant.objects.get(
            activation_code=self.cleaned_data.get('code_for_assigning_ra'))
        hallway = resident_assistant.hallway
        residence_hall = hallway.residence_hall
        Student.objects.create(user=user, resident_assistant=resident_assistant, hallway=hallway,
                               residence_hall=residence_hall)

    # def clean_email(self):
    #     if ATCNUEDU not in self.cleaned_data.get('email'):
    #         raise ValidationError(_(
    #             'This is not a valid Christopher Newport University email address. '
    #             'Please provide the system with a valid email address.'))
    #     return self.cleaned_data.get('email')

    def clean(self):
        try:
            ResidentAssistant.objects.get(activation_code=self.cleaned_data.get('code_for_assigning_ra'))
        except ResidentAssistant.DoesNotExist:
            raise ValidationError(_('This Resident Assistant does not exist. Please enter a valid code.'))

        if self.cleaned_data.get('password') != self.cleaned_data.get('password_confirmation'):
            raise ValidationError(_('Passwords do not match. Please re-enter your password information.'))

        return self.cleaned_data

    class Meta:
        model = User
        fields = ['email', 'student_id', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Email Address')}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Password')}),
            'student_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Student ID')}),
        }


class ResidentAssistantRegistrationForm(ModelForm):
    password_confirmation = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': _('Password Confirmation'), 'id': 'id_password_confirmation'}))
    residence_halls = forms.ModelChoiceField(required=True, queryset=ResidenceHall.objects.all(),
                                             widget=forms.Select(attrs={'class': 'form-control'}))
    hallway_selection = forms.ModelChoiceField(required=True, queryset=Hallway.objects.none(),
                                               widget=forms.Select(attrs={'class': 'form-control'}))
    activation_code = forms.CharField(
        widget=forms.HiddenInput(attrs={'id': 'activation_code', 'value': get_random_string()}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'residence_halls' in self.data:
            try:
                residence_hall_id = int(self.data.get('residence_halls'))
                self.fields['hallway_selection'].queryset = Hallway.objects.filter(
                    residence_hall_id=residence_hall_id).exclude(resident_assistant__isnull=False).order_by('floor')
            except (ValueError, TypeError):
                pass

    # def clean_email(self):
    #     if ATCNUEDU not in self.cleaned_data.get('email'):
    #         raise ValidationError(_(
    #             'This is not a valid Christopher Newport University email address. '
    #             'Please provide the system with a valid email address.'))
    #     return self.cleaned_data.get('email')

    def save(self, commit=True, **kwargs):
        user = super().save(commit=False)
        user.is_resident_assistant = True
        user.set_password(user.password)
        # user.first_name, user.last_name = get_names(self.cleaned_data.get('email'))
        if commit:
            user.save()
            mail_subject = 'Attempted Resident Assistant Registration'
            current_email = self.cleaned_data.get('email')
            plain_text_message = render_to_string('emails/activationcode_email.html', {
                'domain': Site.objects.get_current(),
                'email': current_email,
                'activation_code': self.cleaned_data.get('activation_code'),
                'floor': self.cleaned_data.get('hallway_selection'),
                'uidb64': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            send_mail(subject=mail_subject,
                      message=plain_text_message,
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[current_email])
        ra = ResidentAssistant.objects.create(user=user, residence_hall=self.cleaned_data.get('residence_halls'),
                                              activation_code=self.cleaned_data.get('activation_code'))
        hallway = self.cleaned_data.get('hallway_selection')
        hallway.resident_assistant = ra
        hallway.save()

    def clean(self):
        if self.cleaned_data.get('password') != self.cleaned_data.get('password_confirmation'):
            raise ValidationError(_('Passwords do not match. Please re-enter your password information.'))

        return self.cleaned_data

    class Meta:
        model = User
        fields = ['email', 'student_id', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': _('Email Address')}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': _('Password')}),
            'student_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Student ID')}),
        }
