from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel


class GlobalConfiguration(SingletonModel):
    class Meta:
        verbose_name = _('global_configuration')
        verbose_name_plural = _('global_configurations')
        db_table = 'reference.global_configurations'
