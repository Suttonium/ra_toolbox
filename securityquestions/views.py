from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views.generic import UpdateView
from django.views.generic.base import View

# Create your views here.
from accounts.models import User
from accounts.tokens import account_activation_token
from .forms import *


class CreateSecurityQuestions(View):
    template_name = 'securityquestions/securityquestions_form.html'

    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            form = SecurityQuestionsForm(instance=user.securityquestions)
            context = {'form': form}
            return render(request, self.template_name, context)
        else:
            # rewrite this using messages that displays on the login screen
            return HttpResponse('Activation link is invalid!')

    def post(self, request, uidb64, token):
        form = SecurityQuestionsForm()
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user:
            form = SecurityQuestionsForm(request.POST, instance=user.securityquestions)
            if form.is_valid():
                form.save()
                return redirect(reverse('accounts:login'))
        context = {'form': form}
        return render(request, self.template_name, context)


class SecurityQuestionResponses(LoginRequiredMixin, UpdateView):
    template_name = 'securityquestions/detail_or_update_responses.html'
    form_class = SecurityQuestionsForm
    model = SecurityQuestions

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
            return redirect(reverse('securityquestions:question-responses', args=[form.instance.pk]))
        context = {'form': form}
        return render(request, self.template_name, context)
