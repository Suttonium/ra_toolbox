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
        santoro = None
        rappahannock = None
        cnu_crossing = None
        cnu_landing = None
        tyler = None
        washington = None
        monroe = None
        wilson = None
        madison = None
        harrison = None
        jefferson = None
        taylor = None
        # how to add greek village?

        [york_east.hallway_set.get_or_create(floor=floor) for floor in ye_floor_list]
        [york_west.hallway_set.get_or_create(floor=floor) for floor in yw_floor_list]
        [potomac_north.hallway_set.get_or_create(floor=floor) for floor in pn_floor_list]
        [potomac_south.hallway_set.get_or_create(floor=floor) for floor in ps_floor_list]
        [james_river.hallway_set.get_or_create(floor=floor) for floor in jr_floor_list]
        [warwick.hallway_set.get_or_create(floor=floor) for floor in ww_floor_list]
