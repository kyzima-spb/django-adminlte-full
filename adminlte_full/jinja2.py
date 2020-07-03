from adminlte_base import filters
from adminlte_base import ThemeColor, ThemeLayout
from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment

from .adminlte import manager

from hashlib import md5
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


def gravatar(email, size=200):
    return 'https://www.gravatar.com/avatar/{}?{}'.format(
        md5(email.lower().encode('utf-8')).hexdigest(),
        urlencode({
            's': str(size)
        })
    )


def environment(**options):
    env = Environment(**options)

    for name in filters.__all__:
        env.filters.setdefault(name, getattr(filters, name))

    env.filters.setdefault('gravatar', gravatar)

    env.globals.update({
        'static': static,
        'url': reverse,
        'adminlte': manager,
        # 'adminlte_user': manager.user,
        'ThemeColor': ThemeColor,
        'ThemeLayout': ThemeLayout,
    })

    return env
