from django.views.generic import TemplateView


# Create your views here.
class SignupTypeDecisionView(TemplateView):
    template_name = 'accounts/ra_or_student.html'
