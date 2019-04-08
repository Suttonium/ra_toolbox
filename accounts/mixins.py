from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.base import View


class LogoutRequiredMixin(View):

    def dispatch(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(reverse('403-logout'))
        return super(LogoutRequiredMixin, self).dispatch(*args, **kwargs)
