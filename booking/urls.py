# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.urls import path
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

app_name = 'booking'
urlpatterns = [
    path('table-booking/', views.booking, name='booking'),
    path('submit-booking/', views.booking_submit, name='submit-booking'),
    path('user-panel/', views.user_panel, name='user-panel'),
    path('update-user/<int:id>', views.user_update, name='user-update'),
    path('user-update-submit/<int:id>',
         views.user_update_submit,
         name='user-update-submit'),
    path('booking-delete/<int:id>',
         views.delete_booking,
         name='delete-booking'),
]
