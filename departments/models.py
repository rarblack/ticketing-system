from django.db import models
from django.conf import settings

from locations.models import Location


class Department(models.Model):

    name = models.CharField(max_length=150)

    code = models.CharField(max_length=250)

    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   models.CASCADE,
                                   null=True,
                                   blank=True,
                                   related_name='updated_departments',
                                   related_query_name='updated_department')

    updated_at = models.DateTimeField(null=True,
                                      blank=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   on_delete=models.SET_NULL,
                                   null=True,
                                   related_name='created_departments',
                                   related_query_name='created_department')

    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['code'],
                name='department_department_constraint'
            )
        ]

    def __str__(self):
        return '%s' % (
            self.name
        )
