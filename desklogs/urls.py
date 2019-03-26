from django.urls import path
from desklogs.views import *

urlpatterns = [
    path('guest_log/', GuestLogEntryListView.as_view(), name='guest-log'),
    path('ajax/create_blank_entry/', CreateBlankGuestLogEntry.as_view(), name='ajax-create-blank-entry'),
    path('ajax/update_guestlog_entry/', UpdateGuestlogEntry.as_view(), name='ajax-update-entry'),
    path('ajax/checkout_guestlog_entry/', CheckoutGuestlogEntry.as_view(), name='ajax-checkout-entry'),
    path('ajax/filter_entries/', FilterGuestlogEntries.as_view(), name='ajax-filter-entries'),
    path('equipment_log/', EquipmentLogEntryListView.as_view(), name='equipment-log'),
    path('ajax/create_blank_equipmentlog_entry/', CreateBlankEquipmentLogEntry.as_view(),
         name='ajax-create-blank-equipmentlog-entry'),
    path('ajax/update_equipmentlog_entry/', UpdateEquipmentlogEntry.as_view(), name='ajax-update-equipmentlog-entry'),
    path('ajax/checkin_equipmentlog_entry/', CheckinEquipmentlogEntry.as_view(), name='ajax-checkin-equipmentlog-entry')
]
