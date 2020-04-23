# coding: utf-8

import re
from hashlib import md5
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

from django.forms.utils import flatatt
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.utils.encoding import force_text
from django.templatetags.static import static


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
    def gravatar_url(cls, email, size=200):
        return 'https://www.gravatar.com/avatar/{}?{}'.format(
            md5(email.lower().encode('utf-8')).hexdigest(),
            urlencode({
                's': str(size)
            })
        )

    @classmethod
    def static(cls, path):
        if not path:
            return ''

        absolute = re.match(r'^(http|https|//)', path, re.IGNORECASE)

        return path if absolute else static(path)
