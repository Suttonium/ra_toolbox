from django.urls import path

from feedbacksubmissions.views import FeedbackSubmissionCreateView

urlpatterns = [
    path('feedback_submission/', FeedbackSubmissionCreateView.as_view(), name='feedback_submission'),
]
