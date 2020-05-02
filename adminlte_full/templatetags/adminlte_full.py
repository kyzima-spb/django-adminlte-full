from typing import NamedTuple

from adminlte_base import AdminLTE as Base
from adminlte_base.constants import ALERTS
from django import template
from django.urls import reverse

from ..context_processors import config
from ..menu import Menu, MenuItem
from ..messages import MessagesList
from ..models import MenuModel
from ..notifications import NotificationList
from ..tasks import TaskList
from ..utils import Html


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
    return Html.gravatar_url(email, size)


@register.inclusion_tag(
    name='adminlte.render_flash_messages',
    filename='adminlte_full/markup/flash_messages.html',
    takes_context=True
)
def render_flash_messages(context):
    return {'messages': map(prepare_message, context['messages'])}


@register.inclusion_tag(
    name='adminlte.render_user_panel',
    filename='adminlte_full/markup/user_panel.html',
    takes_context=True
)
def render_user_panel(context):
    user = context['user']
    profile_endpoint = config['ADMINLTE_PROFILE_ENDPOINT']
    return {
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


@register.inclusion_tag('adminlte_full/navbar/messages.html')
def show_messages():
    sender = MessagesList()
    result = sender.show_signal.send(sender)

    if len(result):
        return {
            'messages': sender.messages,
            'total': sender.total,
        }


@register.inclusion_tag('adminlte_full/navbar/notifications.html')
def show_notifications():
    sender = NotificationList()
    result = sender.show_signal.send(sender)

    if len(result):
        return {
            'notifications': sender.notifications,
            'total': sender.total,
        }


@register.inclusion_tag('adminlte_full/sidebar/search-form.html')
def show_search_form():
    return {}


@register.inclusion_tag('adminlte_full/navbar/tasks.html')
def show_tasks():
    sender = TaskList()
    result = sender.show_signal.send(sender)

    if len(result):
        return {
            'tasks': sender.tasks,
            'total': sender.total,
        }
