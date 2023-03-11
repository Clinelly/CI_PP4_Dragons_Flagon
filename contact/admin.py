from django.contrib import admin
from .models import Contact
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ['name', 'email', 'phone', 'message']
    summernote_fields = ('message')
