from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Comment
from django.http import HttpResponseRedirect
# Create your views here.


class CommentList(generic.ListView):
    model = Comment
    queryset = Comment.objects.filter(approved=True).order_by('created_on')
    template_name = 'index.html'


class AboutPage(generic.ListView):
    def get(self, request):
        return render(request, '../templates/about.html')


def gallery(request):
    return render(request, '../templates/gallery.html')


def contact(request):
    return render(request, '../templates/contact.html')
