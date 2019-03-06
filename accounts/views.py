from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView

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


class Roster(LoginRequiredMixin, ListView):
    template_name = 'accounts/roster.html'
    model = Student

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = self.request.user
        if user.is_hall_director:
            context['current_student_list'] = User.objects.get(pk=self.kwargs['pk']).residentassistant.student_set.all()
        if user.is_resident_assistant:
            context['current_student_list'] = user.residentassistant.student_set.all()
        return context


class HallDirectorRARoster(LoginRequiredMixin, ListView):
    template_name = 'accounts/hall_director_ra_roster.html'
    model = ResidentAssistant

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        user = self.request.user
        context['current_ra_list'] = user.halldirector.residentassistant_set.all()
        return context


class ValidateEmailView(View):
    email_input = 'email_input'

    def get(self, request):
        email = request.GET.get(self.email_input)
        try:
            user = User.objects.get(email__iexact=email)
        except User.DoesNotExist:
            user = None
        return HttpResponse(True) if user is not None else HttpResponse(False)


class ValidateStudentID(View):
    student_id_input = 'student_id_val'

    def get(self, request):
        student_id = request.GET.get(self.student_id_input)
        try:
            user = User.objects.get(student_id=student_id)
        except User.DoesNotExist:
            user = None
        return HttpResponse(True) if user is not None else HttpResponse(False)
