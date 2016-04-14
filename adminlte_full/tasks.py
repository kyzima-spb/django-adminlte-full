#!/usr/bin/env python
# -*- coding: utf-8 -*-

import django.dispatch


class Task(object):
    COLOR_AQUA = 'aqua'
    COLOR_GREEN = 'green'
    COLOR_RED = 'red'
    COLOR_YELLOW = 'yellow'

    def __init__(self, title, progress, color=None, uid=None):
        self.__uid = uid
        self.title = title
        self.progress = progress
        self.color = color or self.COLOR_AQUA

    @property
    def uid(self):
        return self.__uid


class TaskList(object):
    show_signal = django.dispatch.Signal()

    def __init__(self):
        self.__tasks = []

    def add_task(self, task):
        if isinstance(task, Task):
            self.__tasks.append(task)

    @property
    def tasks(self):
        return self.__tasks

    @tasks.setter
    def tasks(self, tasks):
        for task in tasks:
            self.add_task(task)

    @property
    def total(self):
        return len(self.tasks)
