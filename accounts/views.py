from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views import View
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


class ActivateResidentAssistantAccount(View):
    template_name = 'accounts/studentinformationcard_form.html'

    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            form = StudentInformationCardForm(instance=user)
            context = {'form': form}
            return render(request, self.template_name, context)
        else:
            # rewrite this using messages thay displays on the login screen
            return HttpResponse('Activation link is invalid!')

    def post(self, request, uidb64, token):
        form = StudentInformationCardForm()
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user:
            form = StudentInformationCardForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                return redirect(reverse('accounts:login'))
        context = {'form': form}
        return render(request, self.template_name, context)
