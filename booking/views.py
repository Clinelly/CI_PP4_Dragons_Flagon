# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render, redirect, reverse, get_object_or_404
from datetime import date, datetime, timedelta
from django.contrib import messages
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import *
from booking.utils import *
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def index(request):
    return render(request, "index.html", {})


def booking(request):
    """
    Calls 'validWeekday' to loop through desired days in the next 21 days.
    Checks if day is valid and shows days that are not full.
    Stores day and service in django session.
    """
    weekdays = validWeekday(22)
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        if service is None:
            messages.success(request, "Please Select A Service!")
            return redirect('booking:booking')

        request.session['day'] = day
        request.session['service'] = service
        request.session['email'] = email
        request.session['phone'] = phone

        return redirect('booking:submit-booking')

    return render(request, '../templates/booking.html', {
            'weekdays': weekdays,
            'validateWeekdays': validateWeekdays,
        })


def booking_submit(request):
    """
    Gets stored data from django session.
    Only shows the times of the day that has not been previously selected.
    Takes the user inputs and creates a booking.
    """
    user = request.user
    times = TIMES
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    service = request.session.get('service')
    email = request.session.get('email')
    phone = request.session.get('phone')

    hour = checkTime(times, day)
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if service is not None:
            if day <= maxDate and day >= minDate:
                if date in ['Monday',
                            'Tuesday',
                            'Wednesday',
                            'Thursday',
                            'Friday',
                            'Saturday',
                            'Sunday']:
                    if TableBooking.objects.filter(day=day).count() < 11:
                        if TableBooking.objects.filter(day=day, time=time)\
                                .count() < 1:
                            BookingForm = TableBooking.objects.get_or_create(
                                user=user,
                                service=service,
                                day=day,
                                time=time,
                                email=email,
                                phone=phone,
                            )
                            messages.success(request, "Booking Saved!")
                            return redirect('home')
                        else:
                            messages.error(request, "Time Reserved Before")
                    else:
                        messages.warning(request, "Selected Day Is Full")
                else:
                    messages.warning(request, "Selected Date Is Incorrect")
            else:
                messages.warning(request, "Date Isn't In Correct Time Period")
        else:
            messages.warning(request, "Select A Service")

    return render(request, '../templates/booking_submit.html', {
        'times': hour,
    })


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


def user_update(request, id):
    """
    Copies the user booking.
    Checks the booking is not 24hrs before the selected time.
    Calls 'validWeekday' to loop through desired days in the next 21 days.
    Checks if day is valid and shows days that are not full.
    Stores day and service in django session.
    """
    booking = TableBooking.objects.get(pk=id)
    userdatepicked = booking.day

    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')

    delta24 = (userdatepicked)\
        .strftime('%Y-%m-%d') >= (today + timedelta(days=1))\
        .strftime('%Y-%m-%d')

    weekdays = validWeekday(22)

    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        request.session['day'] = day
        request.session['service'] = service
        request.session['email'] = email
        request.session['phone'] = phone

        return redirect('booking:user-update-submit', id=id)

    return render(request, '../templates/user_update.html', {
            'weekdays': weekdays,
            'validateWeekdays': validateWeekdays,
            'delta24': delta24,
            'id': id,
        })


def user_update_submit(request, id):
    """
    Gets stored data from django session.
    Only shows the times of the day that has not been previously selected.
    Shows time being edited.
    Takes the user inputs and edits the booking.
    """
    user = request.user
    times = TIMES
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    service = request.session.get('service')
    email = request.session.get('email')
    phone = request.session.get('phone')

    hour = checkEditTime(times, day, id)
    booking = TableBooking.objects.get(pk=id)
    userSelectedTime = booking.time
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if service is not None:
            if day <= maxDate and day >= minDate:
                if date in ['Monday',
                            'Tuesday',
                            'Wednesday',
                            'Thursday',
                            'Friday',
                            'Saturday',
                            'Sunday']:
                    if TableBooking.objects.filter(day=day).count() < 11:
                        if TableBooking.objects.filter(day=day, time=time)\
                                .count() < 1 or userSelectedTime == time:
                            BookingForm = TableBooking.objects.filter(pk=id)\
                                .update(
                                user=user,
                                service=service,
                                day=day,
                                time=time,
                                email=email,
                                phone=phone,
                            )
                            messages.success(request, "Booking Edited!")
                            return redirect('home')
                        else:
                            messages.error(request, "Time Reserved Before")
                    else:
                        messages.warning(request, "Selected Day Is Full")
                else:
                    messages.warning(request, "Selected Date Incorrect")
            else:
                messages.warning(request, "Select A Service")
        else:
            messages.warning(request, "Please Select A Service!")
        return redirect('booking:user-panel')

    return render(request, '../templates/user_update_submit.html', {
        'times': hour,
        'id': id,
    })


def delete_booking(request, id):
    """
    Takes user input and deletes the selected booking.
    """
    booking = TableBooking.objects.get(pk=id)
    userdatepicked = booking.day

    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')

    delta24 = (userdatepicked)\
        .strftime('%Y-%m-%d') >= (today + timedelta(days=1))\
        .strftime('%Y-%m-%d')

    weekdays = validWeekday(22)

    validateWeekdays = isWeekdayValid(weekdays)

    context = {
        'booking': booking,
        'weekdays': weekdays,
        'validateWeekdays': validateWeekdays,
        'delta24': delta24,
        'id': id,
    }
    if request.method == "POST":
        booking.delete()
        messages.success(request, "Booking Deleted")
        return redirect('booking:user-panel')
    return render(request, '../templates/booking_delete.html', context)
