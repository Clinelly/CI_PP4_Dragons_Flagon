from django.shortcuts import render, redirect, reverse, get_object_or_404
from datetime import date, datetime, timedelta
from .models import *
from django.contrib import messages
from django.utils import timezone

def index(request):
    return render(request, "index.html", {})


def booking(request):
    #Calling 'validWeekday' Function to Loop days you want in the next 21 days:
    weekdays = validWeekday(22)

    #Only show the days that are not full:
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        if service is None:
            messages.success(request, "Please Select A Service!")
            return redirect('booking:booking')

        #Store day and service in django session:
        request.session['day'] = day
        request.session['service'] = service
        request.session['email'] = email
        request.session['phone'] = phone

        return redirect('booking:submit-booking')

    return render(request, '../templates/booking.html', {
            'weekdays': weekdays,
            'validateWeekdays': validateWeekdays,
        })


def bookingSubmit(request):
    user = request.user
    times = [
        "12 PM", "1 PM", "2 PM", "3 PM", "4 PM", "5 PM", "6 PM", "7 PM", "8 PM", "9 PM"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    #Get stored data from django session:
    day = request.session.get('day')
    service = request.session.get('service')
    email = request.session.get('email')
    phone = request.session.get('phone')

    #Only show the time of the day that has not been selected before:
    hour = checkTime(times, day)
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if service is not None:
            if day <= maxDate and day >= minDate:
                if date in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
                    if TableBooking.objects.filter(day=day).count() < 11:
                        if TableBooking.objects.filter(day=day, time=time).count() < 1:
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
                            messages.success(request, "The Selected Time Has Been Reserved Before!")
                    else:
                        messages.success(request, "The Selected Day Is Full!")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A Service!")

    return render(request, '../templates/bookingSubmit.html', {
        'times': hour,
    })


def userPanel(request):
    user = request.user
    bookings = TableBooking.objects.filter(user=user).order_by('day', 'time')
    return render(request, '../templates/userPanel.html', {
        'user': user,
        'bookings': bookings,
    })


def userUpdate(request, id):
    booking = TableBooking.objects.get(pk=id)
    userdatepicked = booking.day
    #Copy  booking:
    today = datetime.today()
    minDate = today.strftime('%Y-%m-%d')

    #24h if statement in template:
    delta24 = (userdatepicked).strftime('%Y-%m-%d') >= (today + timedelta(days=1)).strftime('%Y-%m-%d')
    #Calling 'validWeekday' Function to Loop days you want in the next 21 days:
    weekdays = validWeekday(22)

    #Only show the days that are not full:
    validateWeekdays = isWeekdayValid(weekdays)

    if request.method == 'POST':
        service = request.POST.get('service')
        day = request.POST.get('day')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        #Store day and service in django session:
        request.session['day'] = day
        request.session['service'] = service
        request.session['email'] = email
        request.session['phone'] = phone

        return redirect('booking:user-update-submit', id=id)

    return render(request, '../templates/userUpdate.html', {
            'weekdays': weekdays,
            'validateWeekdays': validateWeekdays,
            'delta24': delta24,
            'id': id,
        })


def userUpdateSubmit(request, id):
    user = request.user
    times = [
        "12 PM", "1 PM", "2 PM", "3 PM", "4 PM", "5 PM", "6 PM", "7 PM", "8 PM", "9 PM"
    ]
    today = datetime.now()
    minDate = today.strftime('%Y-%m-%d')
    deltatime = today + timedelta(days=21)
    strdeltatime = deltatime.strftime('%Y-%m-%d')
    maxDate = strdeltatime

    day = request.session.get('day')
    service = request.session.get('service')
    email = request.session.get('email')
    phone = request.session.get('phone')
    
    #Only show the time of the day that has not been selected before and the time he is editing:
    hour = checkEditTime(times, day, id)
    booking = TableBooking.objects.get(pk=id)
    userSelectedTime = booking.time
    if request.method == 'POST':
        time = request.POST.get("time")
        date = dayToWeekday(day)

        if service is not None:
            if day <= maxDate and day >= minDate:
                if date in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
                    if TableBooking.objects.filter(day=day).count() < 11:
                        if TableBooking.objects.filter(day=day, time=time).count() < 1 or userSelectedTime == time:
                            BookingForm = TableBooking.objects.filter(pk=id).update(
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
                            messages.success(request, "The Selected Time Has Been Reserved Before!")
                    else:
                        messages.success(request, "The Selected Day Is Full!")
                else:
                    messages.success(request, "The Selected Date Is Incorrect")
            else:
                messages.success(request, "The Selected Date Isn't In The Correct Time Period!")
        else:
            messages.success(request, "Please Select A Service!")
        return redirect('booking:user-panel')

    return render(request, '../templates/userUpdateSubmit.html', {
        'times': hour,
        'id': id,
    })


def deleteBooking(request, id):
    booking = TableBooking.objects.get(id=id)
    context = {
        'booking': booking
    }
    if request.method == "POST":
        booking.delete()
        return redirect('booking:user-panel')
    return render(request, '../templates/booking_delete.html', context)


def dayToWeekday(x):
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y


def validWeekday(days):
    # Define a set of valid weekdays
    valid_weekdays = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'}

    # Use a list comprehension to generate the list of valid weekdays
    today = date.today()
    weekdays = [str(today + timedelta(days=i)) for i in range(days) if (today + timedelta(days=i)).strftime('%A') in valid_weekdays]

    return weekdays


def isWeekdayValid(x):
    validateWeekdays = []
    for j in x:
        if TableBooking.objects.filter(day=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays


def checkTime(times, day):
    #Only show the time of the day that has not been selected before:
    x = []
    for k in times:
        if TableBooking.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x


def checkEditTime(times, day, id):
    #Only show the time of the day that has not been selected before:
    x = []
    booking = TableBooking.objects.get(pk=id)
    time = booking.time
    for k in times:
        if TableBooking.objects.filter(day=day, time=k).count() < 1 or time == k:
            x.append(k)
    return x
