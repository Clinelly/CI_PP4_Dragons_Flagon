from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from .models import Review, Gallery, Comment
from django.http import HttpResponseRedirect, HttpResponse
from .forms import CommentForm, ReviewForm, ContactForm
from django.utils.text import slugify
from django.core.mail import send_mail, BadHeaderError
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
    else:
        review_form = ReviewForm()
    return render(request, 'review_page.html', {"review_form": ReviewForm()})


#class ReviewLike(View):
    #def post(self, request, slug):
        #post = get_object_or_404(Review, slug=slug)

        #if post.likes.filter(id=request.user.id).exists():
            #post.likes.remove(request.user)
        #else:
            #post.likes.add(request.user)

        #return HttpResponseRedirect(reverse('index', args=[slug]))


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


# def contact(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             subject = "Website Inquiry"
#             body = {
#                 'first_name': form.cleaned_data['first_name'],
#                 'last_name': form.cleaned_data['last_name'],
#                 'email': form.cleaned_data['email_address'],
#                 'message': form.cleaned_data['message'],
#             }
#             message = "\n".join(body.values())

#             try:
#                 send_mail(subject, message, 'freelancer25@msn.com', ['freelancer25@msn.com']) 
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#         return redirect("home")

#     form = ContactForm()
#     return render(request, "../templates/contact.html", {'form': form})


def FoodMenu(request):
    return render(request, '../templates/food_menu.html')


def GameList(request):
    return render(request, '../templates/game_list.html')
