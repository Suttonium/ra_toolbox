from django.contrib.sites.models import Site
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        finalized_domain = Site.objects.all()[0]
        finalized_domain.domain = '127.0.0.1:8000'  # will alter this if pushed to an actual domain name
        finalized_domain.name = 'Local Host'
        finalized_domain.save()
