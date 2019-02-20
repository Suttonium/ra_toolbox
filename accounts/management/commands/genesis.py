from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from django.core.management import BaseCommand
from django.utils.crypto import get_random_string

from accounts.models import User, ResidentAssistant, Student
from residencehalls.models import ResidenceHall, Hallway


class Command(BaseCommand):
    def handle(self, *args, **options):
        finalized_domain = Site.objects.all()[0]
        finalized_domain.domain = '127.0.0.1:8000'  # will alter this if pushed to an actual domain name
        finalized_domain.name = 'Local Host'
        finalized_domain.save()

        student_group, created = Group.objects.get_or_create(name='Student Group')
        resident_assistant_group, created = Group.objects.get_or_create(name='Resident Assistant Group')
        hall_director_group, created = Group.objects.get_or_create(name='Hall Director Group')
        desk_account_group, created = Group.objects.get_or_create(name='Desk Account Group')

        ra_user = User.objects.create_superuser(email='raymond.sutton.15@cnu.edu', student_id='00123456',
                                                password='TEST', is_active=True, is_resident_assistant=True)

        james_river, created = ResidenceHall.objects.get_or_create(name='James River')
        fourth_theme_unit = Hallway.objects.get(floor='4th Floor Theme Unit')

        ra = ResidentAssistant.objects.create(user=ra_user, activation_code='TESTCODE',
                                              residence_hall=james_river)

        fourth_theme_unit.resident_assistant = ra
        fourth_theme_unit.save()

        for i in range(1, 9):
            temp_user = User.objects.create_user(email=get_random_string(), student_id='0000000' + str(i),
                                                 is_active=True,
                                                 is_student=True, is_staff=True, password='TEST')
            Student.objects.create(user=temp_user, resident_assistant=ra, residence_hall=james_river,
                                   hallway=fourth_theme_unit)
