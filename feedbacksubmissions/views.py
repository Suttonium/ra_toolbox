# Create your views here.
from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView

from feedbacksubmissions.forms import FeedbackSubmissionForm
from feedbacksubmissions.models import FeedbackSubmission


class FeedbackSubmissionCreateView(CreateView):
    form_class = FeedbackSubmissionForm
    model = FeedbackSubmission
    template_name = 'feedbacksubmissions/feedbacksubmission_form.html'

    def get_success_url(self):
        messages.success(self.request, 'Feedback Submitted')
        return reverse('accounts:login')
