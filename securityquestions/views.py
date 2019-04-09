from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views.generic import UpdateView
from django.views.generic.base import View
from accounts.models import User
from accounts.tokens import account_activation_token
from .forms import *
from accounts.middleware import *


class CreateSecurityQuestions(View):
    template_name = 'securityquestions/securityquestions_form.html'

    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            security_questions = SecurityQuestions.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, SecurityQuestions.DoesNotExist):
            security_questions = None
        if security_questions is not None and account_activation_token.check_token(security_questions, token):
            user = security_questions.user
            user.is_active = True
            user.save()
            form = SecurityQuestionsForm(instance=security_questions)
            context = {'form': form}
            return render(request, self.template_name, context)
        else:
            messages.error(request, 'The Activation Link is Invalid.')
            return redirect(reverse('accounts:login'))

    def post(self, request, uidb64, token):
        form = SecurityQuestionsForm()
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            security_questions = SecurityQuestions.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, SecurityQuestions.DoesNotExist):
            security_questions = None
        if security_questions:
            form = SecurityQuestionsForm(request.POST, instance=security_questions)
            if form.is_valid():
                form.save()
                messages.success(request,
                                 'Security Questions Saved Successfully for {0}'.format(security_questions.user))
                return redirect(reverse('accounts:login'))
        context = {'form': form}
        return render(request, self.template_name, context)


class SecurityQuestionResponses(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'securityquestions/detail_or_update_responses.html'
    form_class = SecurityQuestionsForm
    model = SecurityQuestions
    permission_required = (
        'securityquestions.change_securityquestions', 'securityquestions.view_securityquestions'
    )

    def get(self, request, **kwargs):
        obj = self.get_object()
        form = SecurityQuestionsForm(instance=obj)
        disable = True
        if obj.favorite_color is None or obj.high_school is None or obj.birth_city is None or \
                obj.favorite_social_media_platform is None or obj.road is None or obj.favorite_food is None:
            disable = False
        context = {'form': form, 'disable_update': True if disable else False, 'user_': obj.user}
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        obj = self.get_object()
        form = SecurityQuestionsForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Security Questions Saved Successfully for {0}'.format(self.get_object().user))
            return redirect(reverse('securityquestions:question-responses', args=[form.instance.pk]))
        context = {'form': form}
        return render(request, self.template_name, context)

    def test_func(self):
        obj = self.get_object()
        user = self.request.user
        return obj.user == self.request.user if not user.is_desk_account else True
