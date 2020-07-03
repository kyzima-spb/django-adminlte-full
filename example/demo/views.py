from datetime import datetime, timedelta

from django.contrib import auth, messages
from django.shortcuts import render
from django import forms
from django.http import JsonResponse
from django.urls import reverse_lazy
from adminlte_base import MenuLoader, MenuItem, Message, Notification, Task, Dropdown, ThemeColor
from adminlte_full.adminlte import manager
from adminlte_full.models import MenuModel


def index(request):
    messages.debug(request, f'Test: {getattr(manager, "test", None)}')
    messages.debug(request, '%s SQL statements were executed.' % 666)
    messages.info(request, 'Three credits remain in your account.')
    messages.success(request, 'Profile details updated.')
    messages.warning(request, 'Your account expires in three days.')
    messages.error(request, 'Document deleted.')
    return render(request, 'adminlte_full/base.html')
    # return render(request, 'breadcrumbs_demo.html')


def profile(request):
    return render(request, 'adminlte_full/base.html')


def terms(request):
    return render(request, 'terms.html')


@manager.menu_loader
class MyMenuLoader(MenuLoader):
    def __call__(self, program_name):
        return MenuModel.objects.get(program_name=program_name)

    # def navbar_menu(self):
    #     return self._create(
    #         self('navbar_menu'),
    #         active_path=self.context['request'].path
    #     )
    #
    # def sidebar_menu(self):
    #     menu = self._create(self('main_menu'), active_path=self.context['request'].path)
    #     menu.get_item(1).add_badge('new', ThemeColor.DANGER)
    #     menu.add_item(
    #         MenuItem('not_db', 'MosgInfo', url='https://mosg.info', icon='far fa-clock')
    #     )
    #     return menu


# @manager.home_page_getter
# def home_page(context):
#     user = context['user']
#
#     if user.username == 'kyzima-spb':
#         return '/blank', 'Dashboard'
#
#     return '/blank', 'Home'


@manager.messages_loader
def load_messages(context):
    now = datetime.now()
    sender = context['user']

    messages = Dropdown('#', 15)
    messages.add(Message(sender, 'Тестовое сообщение 1', '#', sent_at=now - timedelta(seconds=16)),)
    messages.add(Message(sender, 'Тестовое сообщение 2', '#', sent_at=now - timedelta(weeks=2)),)
    messages.add(Message(sender, 'Тестовое сообщение 3', '#'))

    return messages


@manager.notifications_loader
def load_notifications(context):
    notifications = Dropdown('#', 10)
    notifications.add(Notification(
        '4 new messages',
        datetime.now() - timedelta(seconds=16),
        icon='fas fa-envelope',
        color=ThemeColor.SUCCESS
    ))
    notifications.add(Notification(
        '8 friend requests',
        datetime.now() - timedelta(hours=3),
        icon='fas fa-users'
    ))
    notifications.add(Notification(
        '3 new reports',
        icon='fas fa-file',
        color=ThemeColor.DANGER
    ))

    return notifications


@manager.tasks_loader
def load_tasks(context):
    tasks = Dropdown('#')
    tasks.add(Task('Design some buttons', 20, '#'))
    tasks.add(Task('Create a nice theme', 40, '#', color=ThemeColor.SUCCESS))
    tasks.add(Task('Some task I need to do', 60, '#', color=ThemeColor.DANGER))
    tasks.add(Task('Make beautiful transitions', 80, '#', color=ThemeColor.WARNING))
    return tasks
