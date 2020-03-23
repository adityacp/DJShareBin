# Python Imports
import uuid
from functools import partial
from datetime import timedelta

# Django Imports
from django.db import models
from django.utils import timezone
from .lang import languages


class Share(models.Model):
    durations = (
        (0, "Never"), (1, "10 Minutes"), (2, "1 Hour"), (3, "1 Day"),
        (4, "1 Week"), (5, "2 Weeks"), (6, "1 Month"), (7, "6 Months"),
        (8, "1 Year")
    )
    timedeltas = {
        1: partial(timedelta, minutes=10), 2: partial(timedelta, hours=1),
        3: partial(timedelta, days=1), 4: partial(timedelta, days=7),
        5: partial(timedelta, days=14), 6: partial(timedelta, days=30),
        7: partial(timedelta, days=180), 8: partial(timedelta, days=365)
    }
    name = models.CharField(max_length=255)
    text = models.TextField()
    syntax = models.CharField(
        max_length=20, choices=languages, default=languages[117]
    )
    expiry_duration = models.PositiveIntegerField(
        choices=durations, default=durations[0]
    )
    expiry_time = models.DateTimeField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    uid = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=False
    )

    def set_expiry_time(self):
        duration = self.expiry_duration
        if duration != 0:
            self.expiry_time = timezone.now() + self.timedeltas[duration]()

    def get_expiry_time(self):
        return self.expiry_time

    def __str__(self):
        return "Share {0}".format(self.name)
