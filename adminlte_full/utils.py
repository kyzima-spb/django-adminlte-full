#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms.utils import flatatt
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.utils.encoding import force_text
from django.contrib.staticfiles.templatetags.staticfiles import static
import re


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
        if url:
            return cls.tag('link', {
                'rel': 'stylesheet',
                'href': url,
            })
        return ''

    @classmethod
    def js_file(cls, url):
        if url:
            return cls.tag('script', {
                'src': url
            })
        return ''

    @classmethod
    def static(cls, path):
        if not path:
            return ''

        absolute = re.match(r'^(http|https|//)', path, re.IGNORECASE)

        return path if absolute else static(path)
