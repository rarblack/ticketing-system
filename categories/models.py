from django.db import models
from django.conf import settings
from departments.models import Department


class Category(models.Model):

    name = models.CharField(
        max_length=150
    )

    department = models.ForeignKey(
        Department,
        models.CASCADE,
        related_name='categories',
        related_query_name='category'
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
        null=True,
        blank=True,
        related_name='updated_categories',
        related_query_name='updated_category'
    )

    updated_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_categories',
        related_query_name='created_category'
    )

    created_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['name', 'department'],
                name='category_name_department_constraint'
            )
        ]

    def __str__(self):
        return self.name
