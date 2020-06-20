from django.conf import settings
from adminlte_base import ThemeColor, ThemeLayout, DEFAULT_SETTINGS


class ConfigWrapper(object):
    def get(self, name, default=''):
        """Returns the value of any configuration option, or the default value for the AdminLTE options."""
        return getattr(settings, name, DEFAULT_SETTINGS.get(name, default))

    __getitem__ = get


config = ConfigWrapper()


def adminlte(request):
    return {
        'config': config,
        'ThemeColor': ThemeColor,
        'ThemeLayout': ThemeLayout,
        'adminlte_user': request.user,
    }
