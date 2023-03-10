from django.test import TestCase
from tavern.forms import *


class TestTavernForm(TestCase):

    def test_signup_form_first_name(self):
        form = SignupForm({'first_name': ''})
        self.assertFalse(form.is_valid())
    
    def test_signup_form_last_name(self):
        form = SignupForm({'last_name': ''})
        self.assertFalse(form.is_valid())