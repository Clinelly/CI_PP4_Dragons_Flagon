from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from .models import *
from django.contrib import messages


# Create your views here.
def booking_page(request):
    return render(request, "booking.html", {})


def table_booking(request):
    weekdays = validWeekday(31)
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        service = request.POST.get('service')
        date = request.POST.get('date')
        if service is None:
            messages.success(request, "Please select a reson for your visit!")
            return redirect('booking')

        request.session['date'] = date
        request.session['service'] = service
        return redirect(bookingSubmit)

    return render(request, "booking.html", {
        'weekdays': weekdays,
        'validateWeekdays': validateWeekdays,
    })


def bookingSubmit(request):
    user = request.user
    times = [
        "12 PM",
        "1 PM",
        "2 PM",
        "3 PM",
        "4 PM",
        "5 PM",
        "6 PM",
        "7 PM",
        "8 PM",
        "9 PM"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    date = request.session.get('date')
    service = request.session.get('service')

    hour = checkTime(times, date)
    if request.method == 'POST':
        time = request.POST.get("time")
        day = dayToWeekday(date)

        if service is not None:
            AppointmentForm = Appointment.objects.get_or_create(
                user=user,
                service=service,
                day=day,
                time=time,
            )
            messages.success(request, "Booking Saved!")
            return redirect('index')
    return render(request, 'bookingSubmit.html', {'times': hour})


def userPanel(request):
    user = request.user
    bookings = TableBooking.objects.filter(user=user).order_by('Date', 'time')
    return render(request, 'userPanel.html', {
        'user': user,
        'bookings': bookings,
    })


def userUpdate(request, id):
    booking = TableBooking().objects.get(pk=id)
    userdatebooked = booking.day
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')
    delta24 = (userdatebooked).strftime('%Y-%m-%d') >= (today + timedelta(days=1)).strftime('%Y-%m-%d')
    weekdays = validWeekday(32)
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('date')

        request.session['date'] = day
        request.session['service'] = service

        return redirect('userUpdateSubmit', id=id)

    return render(request, 'userUpdate.html', {
            'weekdays': weekdays,
            'validateWeekdays': validateWeekdays,
            'delta24': delta24,
            'id': id,
        })


def userUpdateSubmit(request, id):
    user = request.user
    times = [
        "12 PM",
        "1 PM",
        "2 PM",
        "3 PM",
        "4 PM",
        "5 PM",
        "6 PM",
        "7 PM",
        "8 PM",
        "9 PM"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime
    day = request.session.get('date')
    service = request.session.get('service')
    hour = checkEditTime(times, day, id)
    booking = TableBooking.objects.get(pk=id)
    userSelectedTime = booking.time

    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)
        if service is not None:
            BookingForm = TableBooking.objects.filter(pk=id).update(
                user=user,
                service=service,
                day=day,
                time=time,
            ) 
        messages.success(request, "Appointment Edited!")
        return redirect('index')
    return render(request, 'userUpdateSubmit.html', {
        'times': hour,
        'id': id,
    })


def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y


def validWeekday(days):
    today = datetime.now()
    weekdays = []
    for i in range (0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
    return weekdays


def isWeekdayValid(x):
    validateWeekdays = []
    for j in x:
        if TableBooking.objects.filter(day=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays


def checkTime(times, day):
    x = []
    for k in times:
        if TableBooking.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x


def checkEditTime(times, day, id):
    x = []
    booking = TableBooking.objects.get(pk=id)
    time = appointment.time
    for k in times:
        if TableBooking.objects.filter(day=day, time=k).count() < 1 or time == k:
            x.append(k)
    return x
