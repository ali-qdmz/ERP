from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _



class ProjectManagementConfig(AppConfig):
    name = 'project_management'
    verbose_name = _('مدیریت پروژه')
