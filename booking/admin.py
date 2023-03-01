from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(TableBooking)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('name', 'day', 'time_booked')
    search_fields = ['name', 'day', 'time',]
