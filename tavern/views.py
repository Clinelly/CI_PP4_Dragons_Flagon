from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Review, Gallery, Comment
from django.http import HttpResponseRedirect
from .forms import CommentForm, ReviewForm
# Create your views here.


class ReviewList(generic.ListView):
    model = Review
    queryset = Review.objects.order_by('created_on')
    template_name = 'index.html'
    paginate_by = 12

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_form'] = ReviewForm()
        return context


class ReviewLike(View):
    def post(self, request, slug):
        post = get_object_or_404(Review, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('index', args=[slug]))


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
        comments = gallery.comments.filter(approved=True).order_by('-created_on')
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
        comments = gallery.comments.filter(approved=True).order_by('-created_on')
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


def contact(request):
    return render(request, '../templates/contact.html')


def FoodMenu(request):
    return render(request, '../templates/food_menu.html')


def GameList(request):
    return render(request, '../templates/game_list.html')


def EventPage(request):
    return render(request, '../templates/event_page.html')
