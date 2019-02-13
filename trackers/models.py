from django.db import models


# Create your models here.
class Tracker(models.Model):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE)
    general_information = models.TextField(null=True, default='')
    knock_and_talk_one_information = models.TextField(null=True, default='')
    knock_and_talk_two_information = models.TextField(null=True, default='')
    knock_and_talk_three_information = models.TextField(null=True, default='')
    catch_up_one_information = models.TextField(null=True, default='')
    student_of_concern = models.BooleanField(default=False)

    def __str__(self):
        return 'Tracker for {0}'.format(self.user.email)
