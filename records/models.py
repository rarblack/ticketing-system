from django.db import models
from django.conf import settings

from categories.models import Category
from locations.models import Location


class Record(models.Model):

    name = models.CharField(
        max_length=150
    )

    surname = models.CharField(
        max_length=150
    )

    number = models.CharField(
        max_length=150,
        help_text="+994 xx xxx xx xx"
    )

    location = models.ForeignKey(
        Location,
        null=True,
        on_delete=models.SET_NULL,
        related_name='tickets',
        related_query_name='ticket'
    )

    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        related_name='tickets',
        related_query_name='ticket',
    )

    content = models.TextField()

    status = models.CharField(
        max_length=150,
        choices=[
            ("accept", "accepted"),
            ("pend", "pending"),
            ("reject", "rejected"),
            ("close", "closed"),
        ]
    )

    created_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return '%s->%s' % (
            self.surname,
            self.number
        )
