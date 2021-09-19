from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AttendanceConfig(AppConfig):
    name = 'attendance'
    verbose_name = _('حضور غیاب')
