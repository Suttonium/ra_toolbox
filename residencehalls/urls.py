from django.urls import path
from .views import *

urlpatterns = [
    path('ajax/load-hallways/', LoadHallways.as_view(), name='ajax-load-hallways'),
]
