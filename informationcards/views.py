from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin, PermissionRequiredMixin
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
class ActivateAccount(View):
    template_name = 'informationcards/studentinformationcardpartone_form.html'

    def get(self, request, uidb64, token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            student_information_card = StudentInformationCard.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, StudentInformationCard.DoesNotExist):
            student_information_card = None
        if student_information_card is not None and account_activation_token.check_token(student_information_card,
                                                                                         token):
            user = student_information_card.user
            user.is_active = True
            user.save()
            form = StudentInformationCardPartOneForm(instance=student_information_card)
            context = {'form': form}
            return render(request, self.template_name, context)
        else:
            messages.error(request, 'The Activation Link is Invalid.')
            return redirect(reverse('accounts:login'))

    def post(self, request, uidb64, token):
        form = StudentInformationCardPartOneForm()
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            student_information_card = StudentInformationCard.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, StudentInformationCard.DoesNotExist):
            student_information_card = None
        login(request, student_information_card.user, backend='accounts.backends.EmailBackend')
        if student_information_card:
            form = StudentInformationCardPartOneForm(request.POST, instance=student_information_card)
            if form.is_valid():
                form.save()
                messages.success(request, 'Information Card Part 1 Successfully Saved for {0}'.format(
                    student_information_card.user))
                return redirect(reverse('informationcards:part-two', args=[student_information_card.pk]))
        context = {'form': form}
        return render(request, self.template_name, context)


class UpdateStudentInformationCardPartTwoView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin,
                                              UpdateView):
    template_name = 'informationcards/studentinformationcardparttwo_form.html'
    form_class = StudentInformationCardPartTwoForm
    model = StudentInformationCard
    permission_required = (
        'informationcards.change_studentinformationcard', 'informationcards.view_studentinformationcard'
    )

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
                messages.success(request, 'Information Card Part 2 Successfully Saved for {0}'.format(obj.user))
                return redirect(reverse('informationcards:part-three', args=[form.instance.pk]))
        context = {'form': form}
        return render(request, self.template_name, context)

    def test_func(self):
        return self.get_object().user == self.request.user


class UpdateStudentInformationCardPartOneView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin,
                                              UpdateView):
    template_name = 'informationcards/studentinformationcardpartone_form.html'
    form_class = StudentInformationCardPartOneForm
    model = StudentInformationCard
    permission_required = (
        'informationcards.change_studentinformationcard', 'informationcards.view_studentinformationcard'
    )

    def get(self, request, **kwargs):
        obj = self.get_object()
        form = StudentInformationCardPartOneForm(instance=obj)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, **kwargs):
        obj = self.get_object()
        form = StudentInformationCardPartOneForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Information Card Part 1 Successfully Saved for {0}'.format(obj.user))
            return redirect(reverse('informationcards:part-two', args=[form.instance.pk]))
        context = {'form': form}
        return render(request, self.template_name, context)

    def test_func(self):
        return self.get_object().user == self.request.user


class UpdateStudentInformationCardPartThreeView(LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin,
                                                UpdateView):
    template_name = 'informationcards/studentinformationcardpartthree_form.html'
    form_class = StudentInformationCardPartThreeForm
    model = StudentInformationCard
    permission_required = (
        'informationcards.change_studentinformationcard', 'informationcards.view_studentinformationcard'
    )

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
            logout(request)
            form = StudentInformationCardPartThreeForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                messages.success(request, 'Student Information Card Part 3 Successfully Saved for {0}'.format(obj.user))
                return redirect(reverse('accounts:login'))
        context = {'form': form}
        return render(request, self.template_name, context)

    def test_func(self):
        return self.get_object().user == self.request.user
