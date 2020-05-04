from hashlib import md5
from typing import NamedTuple
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

from adminlte_base import AdminLTE as Base
from adminlte_base.filters import format_date_for_human
from adminlte_base.constants import ALERTS
from django import template
from django.urls import reverse

from .. import navbar
from ..context_processors import config
from ..menu import Menu, MenuItem
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


class AdminLTE(Base):
    def static(self, filename):
        pass


adminlte = AdminLTE()
register = template.Library()


@register.filter
def gravatar(email, size=200):
    return 'https://www.gravatar.com/avatar/{}?{}'.format(
        md5(email.lower().encode('utf-8')).hexdigest(),
        urlencode({
            's': str(size)
        })
    )


@register.filter
def human_date(dt):
    return format_date_for_human(dt)


@register.inclusion_tag(
    name='adminlte.render_flash_messages',
    filename='adminlte_full/markup/flash_messages.html',
    takes_context=True
)
def render_flash_messages(context):
    return {'messages': map(prepare_message, context['messages'])}


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


@register.inclusion_tag(
    filename='adminlte_full/markup/sidebar_menu.html',
    takes_context=True
)
def render_menu(context, program_name):
    data = MenuModel.objects.get(program_name=program_name)
    menu = Menu()

    for i in data.items:
        menu.add_item(MenuItem(
            id_item=i.id,
            title=i.title,
            endpoint=i.endpoint,
            endpoint_args=i.get_endpoint_args(),
            endpoint_kwargs=i.get_endpoint_kwargs(),
            parent=menu.get_item(i.parent and i.parent.id),
            item_type=i.type,
            icon=i.icon,
            help=i.help
        ))

    menu.activate_by_context(context)
    menu.show_signal.send(menu, context=context)

    return {
        'menu': menu,
        'items': menu
    }


# @register.inclusion_tag('adminlte_full/breadcrumb/breadcrumb.html')
# def show_breadcrumb():
#     return {}


@register.inclusion_tag(
    name='adminlte.render_messages',
    filename='adminlte_full/markup/messages_menu.html',
    takes_context=True
)
def render_messages(context, messages):
    sender = navbar.MessageDropdown(context)
    sender.show_signal.send(sender)
    return {
        'messages': sender,
    }


@register.inclusion_tag(
    name='adminlte.render_notifications',
    filename='adminlte_full/markup/notifications_menu.html',
    takes_context=True
)
def show_notifications(context, notifications):
    sender = navbar.NotificationDropdown(context)
    sender.show_signal.send(sender)
    return {
        'notifications': sender,
    }


@register.inclusion_tag(
    name='adminlte.render_tasks',
    filename='adminlte_full/markup/tasks_menu.html',
    takes_context=True
)
def show_tasks(context, tasks):
    sender = navbar.TaskDropdown(context)
    sender.show_signal.send(sender)
    return {
        'tasks': sender,
    }


# @register.inclusion_tag('adminlte_full/sidebar/search-form.html')
# def show_search_form():
#     return {}
