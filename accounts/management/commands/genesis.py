from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from django.core.management import BaseCommand
from django.utils.crypto import get_random_string

from accounts.models import User, ResidentAssistant, Student, HallDirector, DeskAccount
from residencehalls.models import ResidenceHall, Hallway
from accounts.constants import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        finalized_domain = Site.objects.all()[0]
        finalized_domain.domain = '127.0.0.1:8000'  # will alter this if pushed to an actual domain name
        finalized_domain.name = 'Local Host'
        finalized_domain.save()

        # ############GROUPS############
        student_group, created = Group.objects.get_or_create(name='Student Group')
        resident_assistant_group, created = Group.objects.get_or_create(name='Resident Assistant Group')
        hall_director_group, created = Group.objects.get_or_create(name='Hall Director Group')
        desk_account_group, created = Group.objects.get_or_create(name='Desk Account Group')
        ################################

        # #####CREATE HALL DIRECTORS####
        hall_directors = []
        for hd_email in hall_director_list:
            hd_user = User.objects.create_user(email=hd_email, is_active=True, is_hall_director=True, password='TEST')
            hall_directors.append(HallDirector.objects.create(user=hd_user))
        ################################

        # ######ASSIGN HD'S TO HALLS####
        york_east = ResidenceHall.objects.get(name='York East')
        york_east.hall_director = hall_directors[2]
        york_east.save()

        york_west = ResidenceHall.objects.get(name='York West')
        york_west.hall_director = hall_directors[2]
        york_west.save()

        potomac_north = ResidenceHall.objects.get(name='Potomac North')
        potomac_north.hall_director = hall_directors[3]
        potomac_north.save()

        potomac_south = ResidenceHall.objects.get(name='Potomac South')
        potomac_south.hall_director = hall_directors[3]
        potomac_south.save()

        james_river = ResidenceHall.objects.get(name='James River')
        james_river.hall_director = hall_directors[0]
        james_river.save()

        warwick = ResidenceHall.objects.get(name='Warwick')
        warwick.hall_director = hall_directors[6]
        warwick.save()

        santoro = ResidenceHall.objects.get(name='Santoro')
        santoro.hall_director = hall_directors[5]
        santoro.save()
        ################################

        # ######Create Desk Accounts####
        for email in desk_account_email_list:
            user = User.objects.create_user(email=email, password='TEST', is_active=True, is_desk_account=True)
            DeskAccount.objects.create(user=user)
        ################################

        # ######TEST RA AND STUDENTS####
        ra_user = User.objects.create_superuser(email='raymond.sutton.15@cnu.edu', student_id='00123456',
                                                password='TEST', is_active=True, is_resident_assistant=True)

        fourth_theme_unit = Hallway.objects.get(floor='4th Floor Theme Unit')

        ra = ResidentAssistant.objects.create(user=ra_user, activation_code='TESTCODE',
                                              residence_hall=james_river, hall_director=hall_directors[0])

        fourth_theme_unit.resident_assistant = ra
        fourth_theme_unit.save()

        for i in range(1, 9):
            temp_user = User.objects.create_user(email=get_random_string(), student_id='0000000' + str(i),
                                                 is_active=True,
                                                 is_student=True, is_staff=True, password='TEST')
            Student.objects.create(user=temp_user, resident_assistant=ra, residence_hall=james_river,
                                   hallway=fourth_theme_unit)
        ################################
