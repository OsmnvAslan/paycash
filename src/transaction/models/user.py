from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import Entity


class User(Entity):
    name = models.CharField(
        verbose_name=_('name'), help_text=_('name'),
        max_length=18,
    )

    email = models.CharField(
        verbose_name=_('email'), help_text=_('email'),
        max_length=18,
    )

    def __str__(self):
        return '%s - %s - %s' % (self.id, self.name, self.email)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'transaction_user'
