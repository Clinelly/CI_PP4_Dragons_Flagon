from django.contrib import admin
from .models import Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
