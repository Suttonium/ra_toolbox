from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class SecurityQuestions(models.Model):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE)
    favorite_color = models.CharField(max_length=100, null=True)
    high_school = models.CharField(max_length=100, null=True)
    birth_city = models.CharField(max_length=100, null=True)
    favorite_social_media_platform = models.CharField(max_length=100, null=True)
    road = models.CharField(max_length=100, null=True)
    favorite_food = models.CharField(max_length=100, null=True)

    def __str__(self):
        return 'Security Questions for {0}'.format(self.user.email)

    class Meta:
        verbose_name = _('Security Question')
        verbose_name_plural = _('Security Questions')
