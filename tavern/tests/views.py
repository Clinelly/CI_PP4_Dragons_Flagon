from django.test import TestCase, Client
from tavern.models import Review, Gallery, Comment
from django.contrib.auth.models import User
from django.urls import reverse


class TestTavernViews(TestCase):

    def test_about(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '../templates/about.html')

    def test_FoodMenu(self):
        response = self.client.get('/fooddrink/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '../templates/food_menu.html')

    def test_GameList(self):
        response = self.client.get('/games/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '../templates/game_list.html')
