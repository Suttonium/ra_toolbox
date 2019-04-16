from django.utils import timezone


def in_the_future(value):
    if value is not None:
        return value > timezone.now().date()