# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.text import slugify
from django.contrib import messages
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Review, Gallery, Comment
from .forms import CommentForm, ReviewForm, ContactForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create your views here.


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.order_by('created_on')
    template_name = 'index.html'
    paginate_by = 6


def ReviewPage(request):
    queryset = Review.objects.filter(status=1)
    review_form = ReviewForm(data=request.POST)
    if review_form.is_valid():
        review = Review()
        review.slug = slugify(review_form.cleaned_data['title'])
        review.author = request.user
        review.title = request.POST.get('title')
        review.content = request.POST.get('content')
        review.save()
        messages.success(
            request, "Your review has been submitted.")
    else:
        review_form = ReviewForm()
    return render(request, 'review_page.html', {"review_form": ReviewForm()})


def about(request):
    return render(request, '../templates/about.html')


class GalleryList(generic.ListView):
    model = Gallery
    queryset = Gallery.objects.order_by('created_on')
    template_name = 'gallery.html'
    paginate_by = 16


class GalleryDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Gallery.objects.filter(status=1)
        gallery = get_object_or_404(queryset, slug=slug)
        comments = gallery.comments.filter(approved=True)\
            .order_by('-created_on')
        liked = False
        if gallery.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "gallery_detail.html",
            {
                "gallery": gallery,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Gallery.objects.filter(status=1)
        gallery = get_object_or_404(queryset, slug=slug)
        comments = gallery.comments.filter(approved=True)\
            .order_by('-created_on')
        liked = False
        if gallery.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = gallery
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "gallery_detail.html",
            {
                "gallery": gallery,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class GalleryLike(View):
    def post(self, request, slug):
        post = get_object_or_404(Gallery, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('gallery_detail', args=[slug]))


def FoodMenu(request):
    return render(request, '../templates/food_menu.html')


def GameList(request):
    return render(request, '../templates/game_list.html')
