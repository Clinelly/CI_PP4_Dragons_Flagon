# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from datetime import datetime, timedelta
from calendar import HTMLCalendar
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Internal:
from .models import Event
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # Formats a day as a td.
    # Filter events by day.
    def formatday(self, day, events):
        events_per_day = events.filter(start_time__day=day)
        d = ''
        for event in events_per_day:
            d += f'<li> {event.get_html_url} </li>'

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # Formats a week as a tr.
    def formatweek(self, theweek, events):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f'<tr> {week} </tr>'

    # Formats a month as a table.
    # Filter events by year and month.
    def formatmonth(self, withyear=True):
        events = Event.objects.filter(
            start_time__year=self.year,
            start_time__month=self.month
        )

        cal = (f'<table class="calendar table-responsive">\n')
        cal += (
            f'{self.formatmonthname(self.year, self.month, withyear=withyear)}'
            f'\n'
            )
        cal += (f'{self.formatweekheader()}\n')
        for week in self.monthdays2calendar(self.year, self.month):
            cal += (f'{self.formatweek(week, events)}\n')
        cal += (f'</table>\n')
        return cal
