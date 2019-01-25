from django.shortcuts import render

# Create your views here.
from residencehalls.models import Hallway


def load_hallways(request):
    residence_hall_id = request.GET.get('residence_hall')
    hallways = Hallway.objects.filter(residence_hall_id=residence_hall_id).exclude(
        resident_assistant__isnull=False).order_by('floor')
    return render(request, 'ajax/hallway_dropdown_list_options.html', {'hallways': hallways})
