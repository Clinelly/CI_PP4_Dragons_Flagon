from django.shortcuts import render
from django.views import generic
from .models import Comment

# Create your views here.


class CommentList(generic.ListView):
    model = Comment
    queryset = Comment.objects.filter(approved=True).order_by('created_on')
    template_name = 'index.html'
