from django.shortcuts import render
from django.views.generic.base import View

from residencehalls.models import Hallway


# Create your views here.
class LoadHallways(View):
    template_name = 'ajax/hallway_dropdown_list_options.html'

    def get(self, request):
        residence_hall_id = request.GET.get('residence_hall')
        hallways = Hallway.objects.filter(residence_hall_id=residence_hall_id).exclude(
            resident_assistant__isnull=False).order_by('floor')
        return render(request, self.template_name, {'hallways': hallways})
