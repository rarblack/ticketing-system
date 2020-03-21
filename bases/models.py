from django.db import models
from django.conf import settings

from departments.models import Department


def path_to_logoes(instance, filename):
    return '%s/images/logoes/navbar/%s/' % (
        instance.department.code,
        filename
    )


class Navbar(models.Model):

    logo = models.ImageField(upload_to=path_to_logoes)

    type = models.CharField(
        max_length=200,
        default="unauthorized",
        choices=[
            ("unauthorized", 'unauthorized navbar'),
            ("authorized", 'authorized navbar'),
        ]
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
        null=True,
        blank=True,
        related_name='updated_navbars',
        related_query_name='updated_navbar'
    )

    updated_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_navbars',
        related_query_name='created_navbar'
    )

    created_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['logo', 'department'],
                name='navbar_logo_department_constraint'
            )
        ]

    def __str__(self):
        return "%s navbar" % self.type


class Footer(models.Model):

    title = models.CharField(
        max_length=250
    )

    content = models.TextField()

    links = models.ManyToManyField('Link')

    type = models.CharField(
        max_length=200,
        default="unauthorized",
        choices=[
            ("unauthorized", 'unauthorized footer'),
            ("authorized", 'authorized footer'),
        ]
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
        null=True,
        blank=True,
        related_name='updated_footers',
        related_query_name='updated_footer'
    )

    updated_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_footers',
        related_query_name='created_footer'
    )

    created_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['department'],
                name='footer_department_constraint'
            )
        ]

    def __str__(self):
        return "%s footer" % self.type


class Link(models.Model):

    name = models.CharField(
        max_length=100
    )

    url = models.TextField()

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
        null=True,
        blank=True,
        related_name='updated_links',
        related_query_name='updated_link'
    )

    updated_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_links',
        related_query_name='created_link'
    )

    created_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['url'],
                name='link_url_constraint'
            )
        ]

    def __str__(self):
        return "%s" % self.url


