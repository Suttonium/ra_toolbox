from django.urls import path

from informationcards.views import ActivateResidentAssistantAccount

urlpatterns = [
    path('activate/<str:uidb64>/<str:token>', ActivateResidentAssistantAccount.as_view(), name='activate'),
]
