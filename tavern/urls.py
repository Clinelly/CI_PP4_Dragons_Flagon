from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('reviewpage/', views.ReviewPage, name='review_page'),
    path('about/', views.about, name='about'),
    path('gallery/', views.GalleryList.as_view(), name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('fooddrink/', views.FoodMenu, name='fooddrink'),
    path('games/', views.GameList, name='games'),
    path('galllerydetail/<slug:slug>/', views.GalleryDetail.as_view(), name="gallery_detail"),
    path('gallerylike/<slug:slug>/', views.GalleryLike.as_view(), name="gallery_like"),
    #path('reviewlike/<slug:slug>/', views.ReviewLike.as_view(), name="review_like")
]
