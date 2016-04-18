#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms.utils import flatatt
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.utils.encoding import force_text


class Html(object):
    __unpaired = ['link', 'img']

    @classmethod
    def tag(cls, tag, attrs=None, content=None):
        template = '<{tag}{attrs}>' + ('' if tag in cls.__unpaired else '{content}</{tag}>')
        attrs = mark_safe(flatatt(attrs)) if attrs else ''
        content = force_text(content) if content else ''
        return format_html(template, tag=tag, attrs=attrs, content=content)

    @classmethod
    def css_file(cls, url):
        return cls.tag('link', {
            'rel': 'stylesheet',
            'href': url,
        })

    @classmethod
    def js_file(cls, url):
        return cls.tag('script', {
            'src': url
        })
