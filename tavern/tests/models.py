from django.test import TestCase
from tavern.models import Review, Gallery, Comment
from django.contrib.auth.models import User


class TestTavernModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(username='mark', password='mark1')
        testuser2 = User.objects.create_user(username='dave', password='dave1')
        cls.review = Review.objects.create(title="Title", author=testuser1, content='Content', slug='12345')
        cls.gallery = Gallery.objects.create(title="Title2", author=testuser2, content='Content',  slug='54321')
        cls.gallery.likes.set([testuser1.pk, testuser2.pk])
        cls.review.likes.set([testuser1.pk, testuser2.pk])
        cls.post = Gallery.objects.create(title="Title", author=testuser1, content='Content')
        cls.comment = Comment.objects.create(body='body', name='name', post=cls.post)
        cls.expected_string = f"Comment {cls.comment.body} by {cls.comment.name}"

    def test_review_str(self):
        self.assertEquals(str(self.review), "Title")

    def test_review_number_of_likes(self):
        self.assertEquals(self.review.likes.count(), 2)

    def test_gallery_str(self):
        self.assertEquals(str(self.gallery), "Title2")

    def test_gallery_number_of_likes(self):
        self.assertEquals(self.gallery.likes.count(), 2)

    def test_comment_str(self):
        self.assertEqual(str(self.comment), self.expected_string)
