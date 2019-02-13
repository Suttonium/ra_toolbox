from django.urls import path

from trackers.views import *

urlpatterns = [
    path('student_tracker/<int:pk>', StudentTrackerMainView.as_view(), name='student-update-tracker'),
    path('ajax/get_knock_and_talks/', AJAXKnockAndTalks.as_view(), name='ajax-get-knock-and-talks'),
    path('ajax/get_general_information/', AJAXGeneralInformation.as_view(), name='ajax-get-general-information'),
]
