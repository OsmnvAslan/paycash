from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import Entity


class Company(Entity):
    name = models.TextField(
        verbose_name=_('name'),
        help_text=_('name'),
    )
    users = models.ManyToManyField(
        to=User,
        verbose_name=_('user'),
        help_text=_('user'),
        blank=True,
        related_name='companies',
    )

    class Meta:
        db_table = 'common.companies'
        verbose_name = _('company')
        verbose_name_plural = _('companies')

    def __str__(self) -> str:
        return f'{str(self.pk)} - {str(self.name)}'
