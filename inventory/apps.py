from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class InventoryConfig(AppConfig):
    name = 'inventory'
    verbose_name = _('انبار داری')
