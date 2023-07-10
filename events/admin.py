# Register your models here.
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import *
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@admin.register(Event)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('user', 'title', 'description', 'start_time',)
    search_fields = ['user', 'title', 'description', 'start_time', ]
    list_filter = ('user', 'title', 'description', 'start_time',)
