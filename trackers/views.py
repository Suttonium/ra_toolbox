from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from residencehalls.models import Suite, Room
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
        suite = current_tracker_being_viewed.user.student.suite
        room = current_tracker_being_viewed.user.student.room
        room_assignment = str(suite.number) + room.letter
        print(room_assignment)
        context = {'current_tracker': current_tracker_being_viewed, 'room_assignment': room_assignment}
        return render(request, self.template_name, context)


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
            current_tracker.knock_and_talk_three_information = request.GET.get("current_textarea_data")
            current_tracker.save()
        return render(request, self.template_name, {'current_tracker': current_tracker})


class AJAXSubmitGeneralInformation(View):
    template_name = 'trackers/general_information_response.html'

    def get(self, request):
        pk_being_received = request.GET.get('current_site_url_with_pk')[-3:][:-1]
        if '/' in pk_being_received:
            pk_being_received = pk_being_received[-1]
        current_tracker = Tracker.objects.get(pk=pk_being_received)
        suite = current_tracker.user.student.suite
        room = current_tracker.user.student.room
        current_tracker.general_information = request.GET.get("current_textarea_data")
        current_tracker.save()

        room_assignment = str(suite.number) + room.letter

        context = {'current_tracker': current_tracker, 'room_assignment': room_assignment}
        return render(request, self.template_name, context)


class AJAXSubmitRoomAssignment(View):
    template_name = 'trackers/general_information_response.html'

    def get(self, request):
        pk_being_received = request.GET.get('current_site_url_with_pk')[-3:][:-1]
        if '/' in pk_being_received:
            pk_being_received = pk_being_received[-1]
        current_tracker = Tracker.objects.get(pk=pk_being_received)
        text_area_data = request.GET.get('current_room_assignment').replace(' ', '')
        letter = text_area_data[-1]
        last_index = text_area_data.index(letter)
        number = text_area_data[:last_index]
        room_assignment = str(number) + letter
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

        # remove student from any rooms if they are already in one

        potential_room.save()
        current_tracker.user.student.save()

        context = {'current_tracker': current_tracker, 'room_assignment': room_assignment}
        return render(request, self.template_name, context)

