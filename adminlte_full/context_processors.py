from adminlte_base import ThemeColor, ThemeLayout

from .adminlte import config


def adminlte(request):
    return {
        'config': config,
        'ThemeColor': ThemeColor,
        'ThemeLayout': ThemeLayout,
        'adminlte_user': request.user,
    }
