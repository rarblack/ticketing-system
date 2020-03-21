from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from departments.models import Department
from locations.models import Location

from .managers import CustomUserManager
from .validators import CustomEmailValidator


class CustomUser(AbstractUser):

    username = None

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        related_name='department_users',
        related_query_name='department_user'
    )

    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        related_name='location_users',
        related_query_name='location_user'
    )

    email = models.EmailField(
        _('email address'),
        unique=True,
        validators=[CustomEmailValidator],
        help_text=_('Emails ending with socar-aqs.com are only accepted.'),
        error_messages={
            'unique': _("An user with that email already exists."),
        },
    )

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['department', 'location']
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
