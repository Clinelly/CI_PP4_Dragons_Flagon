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
    path('user-panel/', views.user_panel, name='user-panel'),
    path('booking_form/', views.booking_new, name='booking-form'),
    path('booking-edit/<int:booking_id>',
         views.booking_edit,
         name='edit-booking'),
    path('booking-delete/<int:id>',
         views.booking_delete,
         name='delete-booking'),


]
