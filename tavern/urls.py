from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('about', views.about, name='about'),
    path('gallery', views.GalleryList.as_view(), name='gallery'),
    path('contact', views.contact, name='contact'),
    path('fooddrink', views.FoodMenu, name='fooddrink'),
    path('games', views.GameList, name='games'),
    path('events', views.EventPage, name='events')
]
