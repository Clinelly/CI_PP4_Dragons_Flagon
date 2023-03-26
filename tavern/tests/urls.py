from django.test import SimpleTestCase
from django.urls import reverse, resolve
from tavern.views import *


class TestUrls(SimpleTestCase):

    def test_resolve_to_home_page_view(self):
        url = reverse('home')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ReviewList)

    def test_resolve_to_review_page_view(self):
        url = reverse('review_page')
        print(resolve(url))
        self.assertEquals(resolve(url).func, ReviewPage)

    def test_resolve_to_about_page_view(self):
        url = reverse('about')
        print(resolve(url))
        self.assertEquals(resolve(url).func, about)

    def test_resolve_to_gallery_page_view(self):
        url = reverse('gallery')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, GalleryList)

    def test_resolve_to_food_page_view(self):
        url = reverse('fooddrink')
        print(resolve(url))
        self.assertEquals(resolve(url).func, FoodMenu)

    def test_resolve_to_games_page_view(self):
        url = reverse('games')
        print(resolve(url))
        self.assertEquals(resolve(url).func, GameList)

    def test_resolve_to_gallery_detail_page_view(self):
        url = reverse('gallery_detail', args=['slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, GalleryDetail)

    def test_resolve_to_gallery_like_view(self):
        url = reverse('gallery_like', args=['slug'])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, GalleryLike)
