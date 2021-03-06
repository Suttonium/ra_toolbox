from django.urls import path

from informationcards.views import *

urlpatterns = [
    path('activate/<str:uidb64>/<str:token>', ActivateAccount.as_view(), name='activate'),
    path('information_card_part_one/<int:pk>', UpdateStudentInformationCardPartOneView.as_view(), name='part-one'),
    path('information_card_part_two/<int:pk>', UpdateStudentInformationCardPartTwoView.as_view(), name='part-two'),
    path('information_card_part_three/<int:pk>', UpdateStudentInformationCardPartThreeView.as_view(),
         name='part-three'),
    path('student_information_card_overview/<int:pk>', UpdateEntireStudentInformationCardView.as_view(),
         name='overview')
]
