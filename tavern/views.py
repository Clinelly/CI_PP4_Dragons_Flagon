from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Review, Gallery, Comment
from django.http import HttpResponseRedirect
# Create your views here.


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.order_by('created_on')
    template_name = 'index.html'
    paginate_by = 12


def about(request):
    return render(request, '../templates/about.html')


class GalleryList(generic.ListView):
    model = Gallery
    queryset = Gallery.objects.order_by('created_on')
    template_name = 'gallery.html'
    paginate_by = 16


def contact(request):
    return render(request, '../templates/contact.html')


def FoodMenu(request):
    return render(request, '../templates/food_menu.html')


def GameList(request):
    return render(request, '../templates/game_list.html')


def EventPage(request):
    return render(request, '../templates/event_page.html')
