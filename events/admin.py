from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Event)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('title', 'description', 'start_time')
    search_fields = ['title', 'description', 'start_time',]
