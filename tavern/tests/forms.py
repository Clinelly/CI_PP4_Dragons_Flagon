from django.test import TestCase
from tavern.forms import *


class TestTavernFormSignUp(TestCase):

    def test_signup_form_first_name(self):
        form = SignupForm({'first_name': ''})
        self.assertFalse(form.is_valid())

    def test_signup_form_last_name(self):
        form = SignupForm({'last_name': ''})
        self.assertFalse(form.is_valid())

    def test_signup_form_username(self):
        form = SignupForm({'username': ''})
        self.assertFalse(form.is_valid())

    def test_signup_form_password1(self):
        form = SignupForm({'password1': ''})
        self.assertFalse(form.is_valid())

    def test_signup_form_password2(self):
        form = SignupForm({'password2': ''})
        self.assertFalse(form.is_valid())


class TestTavernFormContactForm(TestCase):

    def test_contact_form_first_name(self):
        form = ContactForm({'first_name': ''})
        self.assertFalse(form.is_valid())

    def test_contact_form_last_name(self):
        form = ContactForm({'last_name': ''})
        self.assertFalse(form.is_valid())

    def test_contact_form_email_address(self):
        form = ContactForm({'email_address': ''})
        self.assertFalse(form.is_valid())

    def test_contact_form_message(self):
        form = ContactForm({'message': ''})
        self.assertFalse(form.is_valid())
