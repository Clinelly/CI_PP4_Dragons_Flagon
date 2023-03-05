from . import views
from django.urls import path

app_name = 'booking'
urlpatterns = [
    path('booking/', views.booking, name='booking'),
    path('submit-booking/', views.bookingSubmit, name='bookingSubmit'),
    path('user-panel/', views.userPanel, name='userPanel'),
    path('update-user/<int:id>', views.userUpdate, name='userUpdate'),
    path('user-update-submit/<int:id>', views.userUpdateSubmit, name='userUpdateSubmit'),
]