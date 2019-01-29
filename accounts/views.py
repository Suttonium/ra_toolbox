from django.urls import reverse
from django.views.generic import TemplateView, CreateView

# Create your views here.
from accounts.forms import *


class SignupTypeDecisionView(TemplateView):
    template_name = 'accounts/ra_or_student.html'


class StudentSignUpView(CreateView):
    form_class = StudentRegistrationForm
    model = User
    template_name = 'accounts/studentsignup_form.html'

    def get_success_url(self):
        return reverse('accounts:login')


class ResidentAssistantSignUpView(CreateView):
    form_class = ResidentAssistantRegistrationForm
    model = User
    template_name = 'accounts/residentassistantsignup_form.html'

    def get_success_url(self):
        return reverse('accounts:login')
