from datetime import date, datetime, timedelta
from booking.models import TableBooking

TIMES = [
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


def dayToWeekday(x):
    """
    Takes the day from datetime and returns it as a string.
    """
    z = datetime.strptime(x, "%Y-%m-%d")
    y = z.strftime('%A')
    return y


def validWeekday(days):
    """
    Define a set of valid weekdays.
    Use a list comprehension to generate the list of valid weekdays.
    """

    valid_days = {'Monday',
                  'Tuesday',
                  'Wednesday',
                  'Thursday',
                  'Friday',
                  'Saturday',
                  'Sunday'}

    today = date.today() + timedelta(days=1)
    weekdays = [str(today + timedelta(days=i)) for i in range(days)
                if (today + timedelta(days=i)).strftime('%A') in valid_days]

    return weekdays


def isWeekdayValid(x):
    """
    Checks the weekdays are valid for the booking parameters.
    """
    validateWeekdays = []
    for j in x:
        if TableBooking.objects.filter(day=j).count() < 10:
            validateWeekdays.append(j)
    return validateWeekdays


def checkTime(times, day):
    """
    Shows the time of the day that has not been selected before
    for creating a booking.
    """
    x = []
    for k in times:
        if TableBooking.objects.filter(day=day, time=k).count() < 1:
            x.append(k)
    return x


def checkEditTime(times, day, id):
    """
    Shows the time of the day that has not been selected before
    for creating a booking.
    """
    x = []
    booking = TableBooking.objects.get(pk=id)
    time = booking.time
    for k in times:
        if TableBooking.objects.filter(day=day, time=k)\
                .count() < 1 or time == k:
            x.append(k)
    return x
