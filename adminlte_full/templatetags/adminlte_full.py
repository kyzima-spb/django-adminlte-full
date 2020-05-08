from hashlib import md5
from typing import NamedTuple
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

from adminlte_base import AbstractManager, ALERTS
from adminlte_base import filters
from django import template
from django.urls import reverse, reverse_lazy

from .. import signals
from ..context_processors import config
from ..models import MenuModel


class Message(NamedTuple):
    title: str
    text: str
    level: str
    icon: str
    styles: str


def prepare_message(message):
    level, icon = ALERTS[message.level_tag]
    return Message(message.level_tag, message.message, level, icon, message.extra_tags)


class Manager(AbstractManager):
    def create_url(self, endpoint, endpoint_args=None, endpoint_kwargs=None):
        return reverse_lazy(endpoint, args=endpoint_args, kwargs=endpoint_kwargs)

    def static(self, filename):
        pass


register = template.Library()
manager = Manager()


@manager.menu_loader
def load_menu(program_name):
    return MenuModel.objects.get(program_name=program_name)


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


# @register.inclusion_tag('adminlte_full/breadcrumb/breadcrumb.html')
# def render_breadcrumb():
#     return {}


@register.inclusion_tag(
    name='adminlte.render_flash_messages',
    filename='adminlte_full/markup/flash_messages.html',
    takes_context=True
)
def render_flash_messages(context):
    return {'messages': map(prepare_message, context['messages'])}


@register.inclusion_tag(
    name='adminlte.render_sidebar_menu',
    filename='adminlte_full/markup/sidebar_menu.html',
    takes_context=True
)
@register.inclusion_tag(
    name='adminlte.render_navbar_menu',
    filename='adminlte_full/markup/navbar_menu.html',
    takes_context=True
)
def render_menu(context, program_name):
    menu = manager.get_menu(program_name, context['request'].path)
    signals.menu_loaded.send(menu.__class__, menu=menu, program_name=program_name, context=context)
    return {
        'menu': menu,
        'items': menu
    }


@register.inclusion_tag(
    name='adminlte.render_messages',
    filename='adminlte_full/markup/messages_menu.html',
    takes_context=True
)
def render_messages(context):
    messages = manager.get_incoming_messages(context)
    signals.messages_loaded.send(messages.__class__, messages=messages, context=context)
    return {'messages': messages}


@register.inclusion_tag(
    name='adminlte.render_notifications',
    filename='adminlte_full/markup/notifications_menu.html',
    takes_context=True
)
def render_notifications(context):
    notifications = manager.get_notifications(context)
    signals.notifications_loaded.send(notifications.__class__, notifications=notifications, context=context)
    return {'notifications': notifications}


@register.inclusion_tag(
    name='adminlte.render_tasks',
    filename='adminlte_full/markup/tasks_menu.html',
    takes_context=True
)
def render_tasks(context):
    tasks = manager.get_tasks(context)
    signals.tasks_loaded.send(tasks.__class__, tasks=tasks, context=context)
    return {'tasks': tasks}


@register.inclusion_tag(
    name='adminlte.render_user',
    filename='adminlte_full/markup/user_sidebar_panel.html',
    takes_context=True
)
@register.inclusion_tag(
    name='adminlte.render_legacy_user_menu',
    filename='adminlte_full/markup/legacy_user_menu.html',
    takes_context=True
)
def render_user(context):
    user = context['user']
    profile_endpoint = config['ADMINLTE_PROFILE_ENDPOINT']
    return {
        'config': config,
        'user': user,
        'profile_url': reverse(profile_endpoint, args=(user.id,)),
    }

# @register.inclusion_tag('adminlte_full/sidebar/search-form.html')
# def show_search_form():
#     return {}
