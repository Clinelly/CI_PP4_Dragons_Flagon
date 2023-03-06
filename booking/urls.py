from . import views
from django.urls import path

app_name = 'booking'
urlpatterns = [
    path('table-booking/', views.booking, name='booking'),
    path('submit-booking/', views.bookingSubmit, name='submit-booking'),
    path('user-panel/', views.userPanel, name='user-panel'),
    path('update-user/<int:id>', views.userUpdate, name='user-update'),
    path('user-update-submit/<int:id>', views.userUpdateSubmit, name='user-update-submit'),
    path('booking-delete/<int:id>', views.deleteBooking, name='delete-booking'),
]