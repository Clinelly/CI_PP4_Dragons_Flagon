from django.contrib import admin
from .models import Comment, Review, Gallery
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    search_fields = ['author', 'content']
    summernote_fields = ('content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Gallery)
class GalleryAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content')
