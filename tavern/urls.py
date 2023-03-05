from . import views
from django.urls import path
from booking import urls

urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('gallery/', views.GalleryList.as_view(), name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('fooddrink/', views.FoodMenu, name='fooddrink'),
    path('games/', views.GameList, name='games'),
    # path('events/calendar', views.EventPage, name='events'),
    # path('booking/', views.Booking, name='booking'),
    path('galllerydetail/<slug:slug>/', views.GalleryDetail.as_view(), name="gallery_detail"),
    path('gallerylike/<slug:slug>/', views.GalleryLike.as_view(), name="gallery_like"),
    path('reviewlike/<slug:slug>/', views.ReviewLike.as_view(), name="review_like")
]
