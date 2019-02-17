from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from trackers.forms import TrackerForm
from trackers.models import Tracker


class StudentTrackerMainView(LoginRequiredMixin, DetailView):
    model = Tracker
    template_name = 'trackers/student_tracker.html'
    form_class = TrackerForm


class AJAXKnockAndTalks(View):
    template_name = 'trackers/knock_and_talk_response.html'

    def get(self, request):
        pk_being_received = request.GET.get('pk_being_sent')
        current_tracker_being_viewed = Tracker.objects.get(pk=pk_being_received)
        return render(request, self.template_name, {'current_tracker': current_tracker_being_viewed})


class AJAXGeneralInformation(View):
    template_name = 'trackers/general_information_response.html'

    def get(self, request):
        pk_being_received = request.GET.get('pk_being_sent')
        current_tracker_being_viewed = Tracker.objects.get(pk=pk_being_received)
        return render(request, self.template_name, {'current_tracker': current_tracker_being_viewed})


class AJAXSubmitKnockAndTalk(View):
    template_name = 'trackers/knock_and_talk_response.html'

    def get(self, request):
        pk_being_received = request.GET.get('current_site_url_with_pk')[-3:][:-1]
        if '/' in pk_being_received:
            pk_being_received = pk_being_received[-1]
        current_tracker = Tracker.objects.get(pk=pk_being_received)
        which_knock_and_talk = request.GET.get('which_kat')
        if which_knock_and_talk == str(1):
            current_tracker.knock_and_talk_one_information = request.GET.get("current_textarea_data")
            current_tracker.save()
        if which_knock_and_talk == str(2):
            current_tracker.knock_and_talk_two_information = request.GET.get("current_textarea_data")
            current_tracker.save()
        if which_knock_and_talk == str(3):
            print('HEREEEEEEEEEEEEEEEEEE')
            current_tracker.knock_and_talk_three_information = request.GET.get("current_textarea_data")
            current_tracker.save()
        return render(request, self.template_name, {'current_tracker': current_tracker})
