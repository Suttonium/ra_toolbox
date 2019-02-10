from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from trackers.models import Tracker


class StudentTrackerMainView(LoginRequiredMixin, DetailView):
    model = Tracker
    template_name = 'trackers/student_tracker.html'
    form_class = TrackerForm
