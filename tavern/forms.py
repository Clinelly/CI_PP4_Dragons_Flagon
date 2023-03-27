# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django import forms
from allauth.account.forms import SignupForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Comment, Review
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content',)


class TavernSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)
