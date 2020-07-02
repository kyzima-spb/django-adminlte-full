from hashlib import md5
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

from adminlte_base import filters
from django import template
from django.template import Node
from django.template.base import TemplateSyntaxError, kwarg_re
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from ..adminlte import config
from ..adminlte import manager


register = template.Library()


for name in filters.__all__:
    register.filter(name, getattr(filters, name))


@register.filter
def gravatar(email, size=200):
    return 'https://www.gravatar.com/avatar/{}?{}'.format(
        md5(email.lower().encode('utf-8')).hexdigest(),
        urlencode({
            's': str(size)
        })
    )


@register.filter
def humanize(dt):
    locale = config.get(
        'LOCALE_NAME', config.get('LANGUAGE_CODE').replace('-', '_')
    )
    time_zone = config.get('TIME_ZONE', None)
    return filters.humanize(dt, locale, time_zone)


simple_tag = method_decorator(register.simple_tag)


@register.simple_tag(
    name='adminlte.get_home_page',
    takes_context=True
)
def get_home_page(context):
    """Returns a link to the home page as a named tuple with url and title fields."""
    return manager.with_context(context).get_home_page()


@register.simple_tag(
    name='adminlte.menu.navbar_menu',
    takes_context=True
)
def navbar_menu(context):
    """Creates and returns a navbar menu."""
    return manager.with_context(context).menu.navbar_menu()


@register.simple_tag(
    name='adminlte.menu.sidebar_menu',
    takes_context=True
)
def sidebar_menu(context):
    """Creates and returns a sidebar menu."""
    return manager.with_context(context).menu.sidebar_menu()


@register.inclusion_tag(
    name='adminlte.render_flash_messages',
    filename='adminlte_full/markup/flash_messages.html',
    takes_context=True
)
def render_flash_messages(context):
    """Displays popup messages by category."""
    return {'messages': manager.with_context(context).get_flash_messages()}


@register.inclusion_tag(
    name='adminlte.render_legacy_user_menu',
    filename='adminlte_full/markup/legacy_user_menu.html',
    takes_context=True
)
def render_legacy_user_menu(context):
    """Displays the user menu in the navigation bar in the AdminLTE2 style."""
    return {
        'config': config,
        'user': context['user'],
        'profile_url': reverse_lazy(config['ADMINLTE_PROFILE_ENDPOINT']),
    }


@register.inclusion_tag(
    name='adminlte.render_messages_menu',
    filename='adminlte_full/markup/messages_menu.html',
    takes_context=True
)
def render_messages_menu(context):
    """Displays a dropdown menu with incoming messages."""
    return {'messages': manager.with_context(context).get_incoming_messages()}


@register.inclusion_tag(
    name='adminlte.render_notifications_menu',
    filename='adminlte_full/markup/notifications_menu.html',
    takes_context=True
)
def render_notifications_menu(context):
    """Displays a dropdown menu with notifications."""
    return {'notifications': manager.with_context(context).get_notifications()}


@register.inclusion_tag(
    name='adminlte.render_tasks_menu',
    filename='adminlte_full/markup/tasks_menu.html',
    takes_context=True
)
def render_tasks_menu(context):
    """Displays a dropdown menu with tasks."""
    return {'tasks': manager.with_context(context).get_tasks()}


@register.inclusion_tag(
    name='adminlte.render_language_menu',
    filename='adminlte_full/markup/language_menu.html',
    takes_context=True
)
def render_language_menu(context):
    clone = manager.with_context(context)
    return {
        'current_locale': clone.current_locale,
        'languages': clone.get_available_languages(),
    }


@register.tag(name='breadcrumb')
def do_breadcrumbs(parser, token):
    tag_name, *bits = token.split_contents() # разбивает исходную строку тега по пробелам
    asvar = None

    if len(bits) >= 2 and bits[-2] == 'as': # если есть более двух аргументов и предпоследний из них равен as
        asvar = bits[-1] # тогда результат тега должен быть сохранен в переменную, выставляем флаг
        bits = bits[:-2] # отрезаем as и имя переменной

    args = []
    kwargs = {}

    for bit in bits:
        match = kwarg_re.match(bit) # проверяет, что аргумент корректный: либо позиционный, либо именованный

        if not match: # если совпадений не найдено - синтаксис не корректный
            raise TemplateSyntaxError(f'Malformed arguments to "{tag_name}" tag.')

        name, value = match.groups()

        # compile_filter возвращает FilterExpression,
        # который разбирает токен как переменную с необязательными фильтрами

        if name:
            kwargs[name] = parser.compile_filter(value)
        else:
            args.append(parser.compile_filter(value))

    nodelist = parser.parse(('endbreadcrumb',))
    parser.delete_first_token()

    return BreadcrumbNode(nodelist, *args, asvar=asvar, **kwargs)


class BreadcrumbNode(Node):
    def __init__(self, nodelist, title=None, icon=None, is_active=False, is_safe=False, position=None, asvar=None):
        self.nodelist = nodelist
        self.title = title
        self.icon = icon
        self.is_active = is_active
        self.is_safe = is_safe
        self.position = position
        self.asvar = asvar

    def render(self, context):
        title = f'<span itemprop="name">{self.title.resolve(context)}</span>' if self.title else ''
        icon = f'<i class="{self.icon.resolve(context)}"></i>' if self.icon else ''
        label = f'{icon} {title}'.strip()
        output = self.nodelist.render(context).strip()

        if not output:
            output = f'{label}'
        elif not self.is_safe:
            output = f'<a itemprop="item" href="{output}">{label}</a>'

        if self.position is not None:
            output += f'<meta itemprop="position" content="{self.position}">'

        class_list = 'breadcrumb-item'
        attributes = 'itemprop="itemListElement" itemscope itemtype="http://schema.org/ListItem"'

        if self.is_active:
            class_list += ' active'
            attributes += ' aria-current="page"'

        output = f'<li class="{class_list}" {attributes}>{output}</li>'

        if self.asvar:
            context[self.asvar] = output
            return ''

        return output
