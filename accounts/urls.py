from django.urls import path
from django.contrib.auth import views as auth_views

from accounts.views import *

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/ra_or_student', SignupTypeDecisionView.as_view(), name='ra-or-student'),
    path('register/student', StudentSignUpView.as_view(), name='student-signup'),
    path('register/resident_assistant', ResidentAssistantSignUpView.as_view(), name='ra-signup'),
    path('roster/', Roster.as_view(), name='roster'),
    path('ajax/validate_email/', ValidateEmailView.as_view(), name='ajax-validate-email'),
    path('ajax/validate_student_id/', ValidateStudentID.as_view(), name='ajax-validate-student-id'),
]
