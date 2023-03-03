from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(TableBooking)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('user', 'day', 'time_booked')
    search_fields = ['user', 'day', 'time',]
