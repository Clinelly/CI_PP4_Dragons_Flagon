# Create your models here.
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SERVICE_CHOICES = (
    ("Drinks", "Drinks"),
    ("Food and Drinks", "Food and Drinks"),
    ("Board Game Session", "Board Game Session"),
    ("Food, Drinks and Games", "Food, Drinks and Games"),
    )

TIME_CHOICES = (
    ("12 PM", "12 PM"),
    ("1 PM", "1 PM"),
    ("2 PM", "2 PM"),
    ("3 PM", "3 PM"),
    ("4 PM", "4 PM"),
    ("5 PM", "5 PM"),
    ("6 PM", "6 PM"),
    ("7 PM", "7 PM"),
    ("8 PM", "8 PM"),
    ("9 PM", "9 PM"),
)


class TableBooking(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
        )
    email = models.EmailField()
    service = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES,
        default="Drinks"
        )
    phone = models.IntegerField()
    day = models.DateField(
        default=datetime.now
        )
    time = models.CharField(
        max_length=10,
        choices=TIME_CHOICES,
        default="12 PM")
    time_booked = models.DateTimeField(
        default=datetime.now,
        blank=True)

    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"
