from django.contrib.auth import views as auth_views
from django.urls import path

from accounts.views import *

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/ra_or_student', SignupTypeDecisionView.as_view(), name='ra-or-student'),
    path('register/student', StudentSignUpView.as_view(), name='student-signup'),
    path('register/resident_assistant', ResidentAssistantSignUpView.as_view(), name='ra-signup'),
    path('student_roster/<int:pk>', Roster.as_view(), name='student-roster'),
    path('ra_roster/', HallDirectorRARoster.as_view(), name='ra-roster'),
    path('ajax/validate_email/', ValidateEmailView.as_view(), name='ajax-validate-email'),
    path('ajax/validate_student_id/', ValidateStudentID.as_view(), name='ajax-validate-student-id'),
]
