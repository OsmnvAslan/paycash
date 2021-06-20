from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from .entity import Entity


class Profile(Entity):
    user = models.OneToOneField(
        to=User,
        verbose_name=_('user'),
        help_text=_('user'),
        on_delete=models.CASCADE,
        related_name='profile',
    )

    company = models.ForeignKey(
        to='common.Company',
        on_delete=models.CASCADE,
        verbose_name=_('company'),
        help_text=_('company'),
        null=True,
    )

    position = models.TextField(
        verbose_name=_('position'),
        blank=True,
    )

    department = models.TextField(
        verbose_name=_('department'),
        blank=True,
    )

    class Meta:
        db_table = 'common.profiles'
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')
