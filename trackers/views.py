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
    template_name = 'ajax/knock_and_talk_response.html'

    def get(self, request):
        pk_being_received = request.GET.get('pk_being_sent')
        current_tracker_being_viewed = Tracker.objects.get(pk=pk_being_received)
        return render(request, self.template_name, {'current_tracker': current_tracker_being_viewed})


class AJAXGeneralInformation(View):
    template_name = 'ajax/general_information_response.html'

    def get(self, request):
        pk_being_received = request.GET.get('pk_being_sent')
        current_tracker_being_viewed = Tracker.objects.get(pk=pk_being_received)
        return render(request, self.template_name, {'current_tracker': current_tracker_being_viewed})
