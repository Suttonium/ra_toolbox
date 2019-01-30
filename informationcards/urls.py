from django.urls import path

from informationcards.views import *

urlpatterns = [
    path('activate/<str:uidb64>/<str:token>', ActivateResidentAssistantAccount.as_view(), name='activate'),
    path('information_card_part_one/<int:pk>', UpdateStudentInformationCardPartOneView.as_view(), name='part-one'),
    path('information_card_part_two/<int:pk>', UpdateStudentInformationCardPartTwoView.as_view(), name='part-two'),
]
