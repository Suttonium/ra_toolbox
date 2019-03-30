from django.urls import path

from securityquestions.views import *

urlpatterns = [
    path('answers/<str:uidb64>/<str:token>', CreateSecurityQuestions.as_view(), name='answers'),
]
