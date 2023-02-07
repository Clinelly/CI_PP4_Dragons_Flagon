from . import views
from django.urls import path

urlpatterns = [
    path('', views.CommentList.as_view(), name='home'),
    path('about', views.AboutPage.as_view(), name='about'),
    path('gallery', views.gallery, name='gallery'),
    path('contact', views.contact, name='contact'),
    path('fooddrink', views.FoodMenu, name='fooddrink'),
    path('games', views.GameList, name='games'),
    path('events', views.EventPage, name='events')
]
