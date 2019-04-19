from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class FeedbackSubmission(models.Model):
    email = models.EmailField(_('email address'), blank=False)
    text = models.TextField(null=True, blank=False)

    class Meta:
        verbose_name_plural = 'Feedback Submissions'
        verbose_name = 'Feedback Submission'

    def __str__(self):
        return 'Feedback submitted by {0}'.format(self.email)
