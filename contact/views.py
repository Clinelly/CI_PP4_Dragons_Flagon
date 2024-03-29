# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .forms import ContactForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Gets user information.


def get_user_instance(request):
    """
    Retrieves user details if logged in.
    """

    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()
    return user


# Displays the contact form for the user, autofills their email,
# Checks all data is valid before saving it.


class ContactMessage(View):
    """
    Displays the contact form if the user
    is registered and inserts the user email into the
    email field.
    """
    template_name = '../templates/contact.html'
    success_message = 'Your message has been sent.'

    def get(self, request, *args, **kwargs):
        """
        Retrieves users email and inputs into email input.
        """
        if request.user.is_authenticated:
            email = request.user.email
            contact_form = ContactForm(initial={'email': email})
        else:
            contact_form = ContactForm()
        return render(request, '../templates/contact.html',
                      {'contact_form': contact_form})

    def post(self, request):
        """
        Checks that the provided info is valid format
        and then posts to database.
        """
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.user = request.user
            contact.save()
            messages.success(
                request, "Your message has been sent.")
            return render(request, '../templates/contact.html')

        return render(request, '../templates/contact.html',
                      {'contact_form': contact_form})
