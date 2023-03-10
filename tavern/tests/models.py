from django.test import TestCase
from tavern.models import Review, Gallery, Comment
from django.contrib.auth.models import User


class TestTavernModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')

    def test_review_str(self):
        title = Review.objects.create(title="Title", author=self.user)
        self.assertEquals(str(title), "Title")

    def test_review_like_users(self):
        testuser1 = User.objects.create_user(username='mark', password='mark1')
        testuser2 = User.objects.create_user(username='dave', password='dave1')
        review = Review.objects.create(title="Title", author=self.user, content='Content')
        review.likes.set([testuser1.pk, testuser2.pk])
        self.assertEquals(review.likes.count(), 2)

    def test_gallery_str(self):
        title = Gallery.objects.create(title="Title", author=self.user)
        self.assertEquals(str(title), "Title")

    def test_gallery_like_users(self):
        testuser1 = User.objects.create_user(username='mark', password='mark1')
        testuser2 = User.objects.create_user(username='dave', password='dave1')
        gallery = Gallery.objects.create(title="Title", author=self.user, content='Content')
        gallery.likes.set([testuser1.pk, testuser2.pk])
        self.assertEquals(gallery.likes.count(), 2)

    def test_comment_str(self):
        post = Gallery.objects.create(title="Title", author=self.user, content='Content')
        comment = Comment.objects.create(body='body', name='name', post=post)
        expected_string = f"Comment {comment.body} by {comment.name}"
        self.assertEqual(str(comment), expected_string)
