from django.urls import path
from .views import *

urlpatterns = [
    path('ajax/load-hallways/', load_hallways, name='ajax-load-hallways'),
]
