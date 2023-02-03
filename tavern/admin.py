from django.contrib import admin
from .models import Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('slug', 'created_on')
    search_fields = ['author', 'content']
    prepopulated_fields = {'slug': ('author',)}
    list_filter = ('created_on', 'updated_on')
    summernote_fields = ('content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
