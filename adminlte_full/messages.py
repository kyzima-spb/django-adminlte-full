#!/usr/bin/env python
# -*- coding: utf-8 -*-

import django.dispatch
from django.contrib.auth.models import User
from datetime import datetime, date


class Message(object):
    def __init__(self, sender=None, subject='', sent_at=None, recipient=None, uid=None):
        self.__sender = None
        self.__sent_at = None
        self.__recipient = None

        self.__uid = uid
        self.sender = sender
        self.subject = subject
        self.sent_at = sent_at or datetime.now()
        self.recipient = recipient

    @property
    def uid(self):
        return self.__uid

    @property
    def recipient(self):
        return self.__recipient

    @recipient.setter
    def recipient(self, recipient):
        if isinstance(recipient, User):
            self.__recipient = recipient

    @property
    def sent_at(self):
        return self.__sent_at

    @sent_at.setter
    def sent_at(self, sent_at):
        if not isinstance(sent_at, (date, datetime)):
            sent_at = datetime.strptime(sent_at, '%Y-%m-%d %H:%M:%S')
        self.__sent_at = sent_at

    @property
    def sender(self):
        return self.__sender

    @sender.setter
    def sender(self, sender):
        if isinstance(sender, User):
            self.__sender = sender


class MessagesList(object):
    show_signal = django.dispatch.Signal()

    def __init__(self):
        self.__messages = []

    def add_message(self, message):
        if isinstance(message, Message):
            self.__messages.append(message)

    @property
    def messages(self):
        return self.__messages

    @messages.setter
    def messages(self, messages):
        for msg in messages:
            self.add_message(msg)

    @property
    def total(self):
        return len(self.messages)
