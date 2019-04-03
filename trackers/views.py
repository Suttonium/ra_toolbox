from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from residencehalls.models import Suite, Room
from trackers.forms import TrackerForm
from trackers.models import Tracker
import json


class StudentTrackerMainView(LoginRequiredMixin, DetailView):
    model = Tracker
    template_name = 'trackers/student_tracker.html'
    form_class = TrackerForm


class AJAXKnockAndTalks(LoginRequiredMixin, View):
    template_name = 'trackers/knock_and_talk_response.html'

    def get(self, request):
        pk_being_received = request.GET.get('pk_being_sent')
        current_tracker_being_viewed = Tracker.objects.get(pk=pk_being_received)
        return render(request, self.template_name, {'current_tracker': current_tracker_being_viewed})


class AJAXCatchUps(LoginRequiredMixin, View):
    template_name = 'trackers/catch_up_response.html'

    def get(self, request):
        pk_being_received = request.GET.get('pk_being_sent')
        current_tracker_being_viewed = Tracker.objects.get(pk=pk_being_received)
        return render(request, self.template_name, {'current_tracker': current_tracker_being_viewed})


class AJAXGeneralInformation(LoginRequiredMixin, View):
    template_name = 'trackers/general_information_response.html'

    def get(self, request):
        pk_being_received = request.GET.get('pk_being_sent')
        current_tracker_being_viewed = Tracker.objects.get(pk=pk_being_received)
        suite = current_tracker_being_viewed.user.student.suite
        room = current_tracker_being_viewed.user.student.room
        room_assignment = str(suite.number) + room.letter if suite and room else None
        context = {'current_tracker': current_tracker_being_viewed, 'room_assignment': room_assignment}
        return render(request, self.template_name, context)


class AJAXSubmitKnockAndTalk(LoginRequiredMixin, View):
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
            current_tracker.knock_and_talk_three_information = request.GET.get("current_textarea_data")
            current_tracker.save()
        return render(request, self.template_name, {'current_tracker': current_tracker})


class AJAXSubmitCatchUp(LoginRequiredMixin, View):
    content_type = 'application/json'

    def get(self, request):
        pk_being_received = request.GET.get('current_site_url_with_pk')[-3:][:-1]
        if '/' in pk_being_received:
            pk_being_received = pk_being_received[-1]
        current_tracker = Tracker.objects.get(pk=pk_being_received)
        current_tracker.catch_up_one_information = request.GET.get("current_textarea_data")
        current_tracker.save()
        data = json.dumps({'catch_up_one': current_tracker.catch_up_one_information})
        return HttpResponse(data, content_type=self.content_type)


class AJAXSubmitGeneralInformation(LoginRequiredMixin, View):
    content_type = 'application/json'

    def get(self, request):
        pk_being_received = request.GET.get('current_site_url_with_pk')[-3:][:-1]
        if '/' in pk_being_received:
            pk_being_received = pk_being_received[-1]
        current_tracker = Tracker.objects.get(pk=pk_being_received)
        current_tracker.general_information = request.GET.get("current_textarea_data")
        current_tracker.save()
        data = json.dumps({'general_information': current_tracker.general_information})
        return HttpResponse(data, content_type=self.content_type)


class AJAXSubmitRoomAssignment(LoginRequiredMixin, View):
    context_type = 'application/json'

    def get(self, request):
        pk_being_received = request.GET.get('current_site_url_with_pk')[-3:][:-1]
        if '/' in pk_being_received:
            pk_being_received = pk_being_received[-1]
        current_tracker = Tracker.objects.get(pk=pk_being_received)
        text_area_data = request.GET.get('current_room_assignment').replace(' ', '')
        letter = text_area_data[-1]
        last_index = text_area_data.index(letter)
        number = text_area_data[:last_index]
        suite, created = Suite.objects.get_or_create(number=number, hallway=current_tracker.user.student.hallway,
                                                     residence_hall=current_tracker.user.student.residence_hall)
        potential_room, created = Room.objects.get_or_create(letter=letter, suite=suite,
                                                             residence_hall=current_tracker.user.student.residence_hall)
        if potential_room in suite.room_set.all():
            if current_tracker.user.student not in potential_room.student_set.all():
                current_tracker.user.student.room = potential_room
                current_tracker.user.student.suite = suite
        else:
            potential_room.suite = suite
            current_tracker.user.student.room = potential_room
            current_tracker.user.student.suite = suite

        [current_tracker.user.student.roommates.add(student) for student in potential_room.student_set.all()]
        [current_tracker.user.student.suitemates.add(student) for student in suite.student_set.all()]

        potential_room.save()

        room_assignment = str(number) + letter if suite and potential_room else None
        current_tracker.user.student.save()

        data = json.dumps({'room_assignment': room_assignment})
        return HttpResponse(data, content_type=self.context_type)


class AJAXStudentOfConcernDecision(LoginRequiredMixin, View):
    template_name = 'trackers/student_of_concern_ajax_response.html'

    def get(self, request):
        pk_being_received = request.GET.get('current_site_url_with_pk')[-3:][:-1]
        if '/' in pk_being_received:
            pk_being_received = pk_being_received[-1]
        current_tracker = Tracker.objects.get(pk=pk_being_received)

        if request.GET.get('activate'):
            current_tracker.student_of_concern = True
            current_tracker.save()
        if request.GET.get('deactivate'):
            current_tracker.student_of_concern = False
            current_tracker.save()

        context = {'current_tracker': current_tracker}
        return render(request, self.template_name, context)
