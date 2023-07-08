# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect, reverse, get_object_or_404
from datetime import date, datetime, timedelta
from django.contrib import messages
from django.views import View
from django.core.exceptions import PermissionDenied

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import *
from .forms import *
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def index(request):
    return render(request, "index.html", {})


def user_panel(request):
    """
    Takes the user data and bookings.
    Displays to the user in the user panel template.
    """
    user = request.user
    bookings = TableBooking.objects.filter(user=user).order_by('day', 'time')
    return render(request, '../templates/user_panel.html', {
        'user': user,
        'bookings': bookings,
    })


def booking_new(request, booking_id=None):
    user = request.user
    instance = TableBooking()

    if booking_id:
        instance = get_object_or_404(TableBooking, pk=booking_id)

    booking_form = BookingForm(request.POST or None, instance=instance)

    if request.POST and booking_form.is_valid():
        booking = booking_form.save(commit=False)
        booking.user = user
        booking.save()
        messages.success(request, "New booking created!")
        return redirect('home')

    context = {
        'user': user,
        'booking_form': booking_form,
        'booking': instance
    }
    return render(request, 'booking_form.html', context)


def booking_edit(request, booking_id=None):
    user = request.user
    instance = TableBooking.objects.get(pk=booking_id)

    if instance.user != user:
        raise PermissionDenied()

    form = BookingForm(request.POST or None, instance=instance)

    if request.POST and form.is_valid():
        booking = form.save(commit=False)
        booking.user = user
        booking.save()
        messages.success(request, "Booking updated.")
        return redirect('booking:user-panel')

    context = {
        'user': user,
        'booking_form': form,
        'booking': instance
    }
    return render(request, 'booking_edit.html', context)


def booking_delete(request, id):
    user = request.user
    booking = get_object_or_404(TableBooking, pk=id)

    if booking.user != user:
        raise PermissionDenied()

    if request.method == 'POST':
        booking.user = user
        booking.delete()
        messages.success(
            request, "Booking deleted.")
        return redirect('home')
    context = {
        'booking': booking
    }
    return render(request, 'booking_delete.html', context)


def handle_permission_denied(request, exception):
    return render(request, '403.html', status=403)


# 403 handler
handler403 = handle_permission_denied
