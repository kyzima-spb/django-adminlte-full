#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import template
from django.contrib.staticfiles.templatetags.staticfiles import static
from ..assets import ASSETS
from ..utils import Html
from adminlte_full.messages import MessagesList
from adminlte_full.notifications import NotificationList
from adminlte_full.tasks import TaskList
from adminlte_full.menu import Menu


register = template.Library()


@register.simple_tag
def link_css(name):
    name = '{}_css'.format(name.lower())
    url = ASSETS.get(name, name)
    return Html.css_file(static(url)) if url else ''


@register.simple_tag
def link_js(name):
    print('JS: ', name)
    name = '{}_js'.format(name.lower())
    url = ASSETS.get(name, name)
    return Html.js_file(static(url)) if url else ''


# @register.inclusion_tag('adminlte_full/breadcrumb/breadcrumb.html')
# def show_breadcrumb():
#     return {}


@register.inclusion_tag('adminlte_full/sidebar/menu.html', takes_context=True)
def show_menu(context):
    sender = Menu()
    sender.show_signal.send(sender)
    sender.activate_by_context(context)

    return {
        'menu': sender.items
    }


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


@register.inclusion_tag('adminlte_full/navbar/user.html', takes_context=True)
def show_user(context):
    return {
        'user': context.get('request').user # ????
    }

# @register.inclusion_tag('adminlte_full/sidebar/user-panel.html')
# def show_user_panel():
#     return {}
