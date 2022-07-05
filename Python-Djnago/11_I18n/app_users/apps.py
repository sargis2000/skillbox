from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppUserConfig(AppConfig):
    name = 'app_users'
    verbose_name = _('app_users')
    verbose_name_plural = _('app_users')