from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

import hr.apps


class CrmConfig(AppConfig):
    name = 'crm'
    verbose_name = _('مدیریت ارتباطات مشتریان')
