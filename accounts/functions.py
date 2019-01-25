from django.core.mail import EmailMessage
from django.utils.crypto import get_random_string

from accounts.models import ResidentAssistant


def get_names(email):
    return map(lambda x: x.title(), email.split('.')[:2])


def generate_activation_code():
    activation_code = get_random_string()
    if any(ra.activation_code == activation_code for ra in ResidentAssistant.objects.all()):
        generate_activation_code()
    return activation_code


def send_email(subject, email, message):
    sent_email = EmailMessage(subject, message, to=[email])
    sent_email.send()

