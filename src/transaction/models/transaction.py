from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import Entity


class Transaction(Entity):
    STATUSES = (
        ('deposit', 'DEPOSIT'),
        ('withdraw', 'WITHDRAW'),
    )
    user = models.ForeignKey(
        to='transaction.User', on_delete=models.SET_NULL,
        null=True, related_name='payment',
        verbose_name=_('user'), help_text=_('user'),
    )
    total = models.SmallIntegerField(
        verbose_name=_('total'), help_text=_('total'),
    )
    status = models.CharField(
        verbose_name=_('status'), help_text=_('status'),
        max_length=18, choices=STATUSES, default='deposit'
    )

    def __str__(self):
        return '%s - %s - %s'  % (self.user, self.total, self.status)

    class Meta:
        verbose_name = _('transaction')
        verbose_name_plural = _('transactions')
        db_table = 'transaction_payments'
