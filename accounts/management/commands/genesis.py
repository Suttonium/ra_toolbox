from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from django.core.management import BaseCommand


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
