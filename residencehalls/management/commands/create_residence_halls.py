from django.core.management import BaseCommand

from residencehalls.constants import *
from residencehalls.models import ResidenceHall


class Command(BaseCommand):
    def handle(self, *args, **options):
        [ResidenceHall.objects.get_or_create(name=name) for name in residence_hall_list]

        york_east = ResidenceHall.objects.get(name='York East')
        york_west = ResidenceHall.objects.get(name='York West')
        potomac_north = ResidenceHall.objects.get(name='Potomac North')
        potomac_south = ResidenceHall.objects.get(name='Potomac South')
        james_river = ResidenceHall.objects.get(name='James River')
        warwick = ResidenceHall.objects.get(name='Warwick')
        santoro = ResidenceHall.objects.get(name='Santoro')
        rappahannock = ResidenceHall.objects.get(name='Rappahannock')
        tyler = ResidenceHall.objects.get(name='Tyler')
        washington = ResidenceHall.objects.get(name='Washington')
        monroe = ResidenceHall.objects.get(name='Monroe')
        wilson = ResidenceHall.objects.get(name='Wilson')
        madison = ResidenceHall.objects.get(name='Madison')
        harrison = ResidenceHall.objects.get(name='Harrison')
        jefferson = ResidenceHall.objects.get(name='Jefferson')
        taylor = ResidenceHall.objects.get(name='Taylor')

        [york_east.hallway_set.get_or_create(floor=floor) for floor in ye_floor_list]
        [york_west.hallway_set.get_or_create(floor=floor) for floor in yw_floor_list]
        [potomac_north.hallway_set.get_or_create(floor=floor) for floor in pn_floor_list]
        [potomac_south.hallway_set.get_or_create(floor=floor) for floor in ps_floor_list]
        [james_river.hallway_set.get_or_create(floor=floor) for floor in jr_floor_list]
        [warwick.hallway_set.get_or_create(floor=floor) for floor in ww_floor_list]
        [santoro.hallway_set.get_or_create(floor=floor) for floor in toro_floor_list]
