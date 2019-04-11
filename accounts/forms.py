from django import forms
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.db import IntegrityError
from django.forms import ModelForm
from django.template.loader import get_template
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import ugettext_lazy as _

from accounts.tokens import account_activation_token
from capstone import settings
from residencehalls.models import ResidenceHall, Hallway
from .constants import ACTIVATION_CODE_LIMIT
from .functions import *
from .models import User, Student


class StudentRegistrationForm(ModelForm):
    code_for_assigning_ra = forms.CharField(required=True, max_length=ACTIVATION_CODE_LIMIT, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'id_code_for_assigning_ra', 'placeholder': _('Activation Code')}))
    password_confirmation = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': _('Password Confirmation'), 'id': 'id_password_confirmation'}))

    def save(self, commit=True, **kwargs):
        user = super().save(commit=False)
        user.is_student = True
        user.is_active = True
        user.set_password(user.password)
        # user.first_name, user.last_name = get_names(self.cleaned_data.get('email'))
        if commit:
            user.save()
            mail_subject = 'Attempted Resident Assistant Registration: Student Information Card'
            current_email = self.cleaned_data.get('email')
            plain_text = get_template('emails/txt/student_signup_email_student_information_card.txt')
            htmly = get_template('emails/html/student_signup_email_student_information_card.html')
            context = {
                'domain': Site.objects.get_current(),
                'email': current_email,
                'activation_code': self.cleaned_data.get('activation_code'),
                'floor': self.cleaned_data.get('hallway_selection'),
                'uidb64': urlsafe_base64_encode(force_bytes(user.studentinformationcard.pk)).decode(),
                'token': account_activation_token.make_token(user.studentinformationcard),
            }
            text_content = plain_text.render(context)
            html_content = htmly.render(context)
            message = EmailMultiAlternatives(mail_subject, text_content, settings.EMAIL_HOST_USER, [current_email])
            message.attach_alternative(html_content, 'text/html')
            message.send()

            mail_subject = 'Attempted Resident Assistant Registration: Security Questions'
            current_email = self.cleaned_data.get('email')
            plain_text = get_template('emails/txt/student_email_security_questions.txt')
            htmly = get_template('emails/html/student_signup_email_security_questions.html')
            context = {
                'domain': Site.objects.get_current(),
                'email': current_email,
                'activation_code': self.cleaned_data.get('activation_code'),
                'floor': self.cleaned_data.get('hallway_selection'),
                'uidb64': urlsafe_base64_encode(force_bytes(user.securityquestions.pk)).decode(),
                'token': account_activation_token.make_token(user.securityquestions),
            }
            text_content = plain_text.render(context)
            html_content = htmly.render(context)
            message = EmailMultiAlternatives(mail_subject, text_content, settings.EMAIL_HOST_USER, [current_email])
            message.attach_alternative(html_content, 'text/html')
            message.send()
        resident_assistant = ResidentAssistant.objects.get(
            activation_code=self.cleaned_data.get('code_for_assigning_ra'))
        hallway = resident_assistant.hallway
        residence_hall = hallway.residence_hall
        Student.objects.create(user=user, resident_assistant=resident_assistant, hallway=hallway,
                               residence_hall=residence_hall)

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except IntegrityError:
            raise ValidationError(_('This email is already in use. Please provide the system with another email.'))
        except User.DoesNotExist:
            return email
        raise ValidationError(_('This email is already in use. Please provide the system with another email.'))

    def clean_student_id(self):
        student_id = self.cleaned_data['student_id']
        try:
            User.objects.get(student_id=student_id)
        except IntegrityError:
            raise ValidationError(
                _('This student ID is already in use. Please provide the system with another student ID.'))
        except User.DoesNotExist:
            return student_id
        raise ValidationError(
            _('This student ID is already in use. Please provide the system with another student ID.'))

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
        widget=forms.HiddenInput(attrs={'id': 'activation_code', 'value': generate_activation_code()}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'residence_halls' in self.data:
            try:
                residence_hall_id = int(self.data.get('residence_halls'))
                self.fields['hallway_selection'].queryset = Hallway.objects.filter(
                    residence_hall_id=residence_hall_id).exclude(resident_assistant__isnull=False).order_by('floor')
            except (ValueError, TypeError):
                pass

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
        except IntegrityError:
            raise ValidationError(_('This email is already in use. Please provide the system with another email.'))
        except User.DoesNotExist:
            return email
        raise ValidationError(_('This email is already in use. Please provide the system with another email.'))

    def clean_student_id(self):
        student_id = self.cleaned_data['student_id']
        try:
            User.objects.get(student_id=student_id)
        except IntegrityError:
            raise ValidationError(
                _('This student ID is already in use. Please provide the system with another student ID.'))
        except User.DoesNotExist:
            return student_id
        raise ValidationError(
            _('This student ID is already in use. Please provide the system with another student ID.'))

    def save(self, commit=True, **kwargs):
        user = super().save(commit=False)
        user.is_resident_assistant = True
        user.is_active = True
        user.set_password(user.password)
        # user.first_name, user.last_name = get_names(self.cleaned_data.get('email'))
        if commit:
            user.save()
            mail_subject = 'Attempted Resident Assistant Registration: Student Information Card'
            current_email = self.cleaned_data.get('email')
            plain_text = get_template('emails/txt/ra_signup_email_student_information_card.txt')
            htmly = get_template('emails/html/ra_signup_email_student_information_card.html')
            context = {
                'domain': Site.objects.get_current(),
                'email': current_email,
                'activation_code': self.cleaned_data.get('activation_code'),
                'floor': self.cleaned_data.get('hallway_selection'),
                'uidb64': urlsafe_base64_encode(force_bytes(user.studentinformationcard.pk)).decode(),
                'token': account_activation_token.make_token(user.studentinformationcard),
            }
            text_content = plain_text.render(context)
            html_content = htmly.render(context)
            message = EmailMultiAlternatives(mail_subject, text_content, settings.EMAIL_HOST_USER, [current_email])
            message.attach_alternative(html_content, 'text/html')
            message.send()

            mail_subject = 'Attempted Resident Assistant Registration: Security Questions'
            current_email = self.cleaned_data.get('email')
            plain_text = get_template('emails/txt/ra_signup_email_security_questions.txt')
            htmly = get_template('emails/html/ra_signup_email_security_questions.html')
            context = {
                'domain': Site.objects.get_current(),
                'email': current_email,
                'activation_code': self.cleaned_data.get('activation_code'),
                'floor': self.cleaned_data.get('hallway_selection'),
                'uidb64': urlsafe_base64_encode(force_bytes(user.securityquestions.pk)).decode(),
                'token': account_activation_token.make_token(user.securityquestions),
            }
            text_content = plain_text.render(context)
            html_content = htmly.render(context)
            message = EmailMultiAlternatives(mail_subject, text_content, settings.EMAIL_HOST_USER, [current_email])
            message.attach_alternative(html_content, 'text/html')
            message.send()

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
