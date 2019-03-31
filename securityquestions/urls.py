from django.urls import path

from securityquestions.views import *

urlpatterns = [
    path('questions/<str:uidb64>/<str:token>', CreateSecurityQuestions.as_view(), name='answers'),
    path('question_responses/<int:pk>', SecurityQuestionResponses.as_view(), name='question-responses'),
]
