from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.views.generic import UpdateView
from django.views.generic.base import View

from accounts.models import User
from accounts.tokens import account_activation_token
from informationcards.forms import *


# Create your views here.
class ActivateResidentAssistantAccount(View):
    template_name = 'informationcards/studentinformationcardpartone_form.html'

    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            form = StudentInformationCardPartOneForm(instance=user.studentinformationcard)
            context = {'form': form}
            return render(request, self.template_name, context)
        else:
            # rewrite this using messages that displays on the login screen
            return HttpResponse('Activation link is invalid!')

    def post(self, request, uidb64, token):
        form = StudentInformationCardPartOneForm()
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user:
            form = StudentInformationCardPartOneForm(request.POST, instance=user.studentinformationcard)
            if form.is_valid():
                form.save()
                return redirect(reverse('informationcards:part-two', args=[user.studentinformationcard.pk]))
        context = {'form': form}
        return render(request, self.template_name, context)


class UpdateStudentInformationCardPartTwoView(UpdateView):
    template_name = 'informationcards/studentinformationcardparttwo_form.html'
    form_class = StudentInformationCardPartTwoForm
    model = StudentInformationCard

    def get(self, request, **kwargs):
        obj = self.get_object()
        form = StudentInformationCardPartTwoForm(instance=obj)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        obj = self.get_object()
        form = StudentInformationCardPartTwoForm(instance=obj)
        if request.POST.get('previous_page'):
            form = StudentInformationCardPartTwoForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect(reverse('informationcards:part-one', args=[form.instance.pk]))
        elif request.POST.get('next_page'):
            form = StudentInformationCardPartTwoForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect(reverse('informationcards:part-three', args=[form.instance.pk]))
        context = {'form': form}
        return render(request, self.template_name, context)


class UpdateStudentInformationCardPartOneView(UpdateView):
    template_name = 'informationcards/studentinformationcardpartone_form.html'
    form_class = StudentInformationCardPartOneForm
    model = StudentInformationCard

    def get_success_url(self):
        return reverse('informationcards:part-two', args=[self.object.id])


class UpdateStudentInformationCardPartThreeView(UpdateView):
    template_name = 'informationcards/studentinformationcardpartthree_form.html'
    form_class = StudentInformationCardPartThreeForm
    model = StudentInformationCard

    def get(self, request, **kwargs):
        obj = self.get_object()
        form = StudentInformationCardPartThreeForm(instance=obj)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        obj = self.get_object()
        form = StudentInformationCardPartThreeForm(instance=obj)
        if request.POST.get('previous_page'):
            form = StudentInformationCardPartThreeForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect(reverse('informationcards:part-two', args=[form.instance.pk]))
        elif request.POST.get('submit'):
            form = StudentInformationCardPartThreeForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                # add message here with successmessage mixin to display on login page
                return redirect(reverse('accounts:login'))
        context = {'form': form}
        return render(request, self.template_name, context)
