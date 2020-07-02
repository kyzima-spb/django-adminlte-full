from adminlte_base import (
    AbstractManager, FlashedMessage, MenuLoader, Dropdown, Error,
    ThemeColor, ThemeLayout, DEFAULT_SETTINGS
)
from django.conf import settings
from django.urls import reverse_lazy


class ConfigWrapper(object):
    def get(self, name, default=''):
        """Returns the value of any configuration option, or the default value for the AdminLTE options."""
        return getattr(settings, name, DEFAULT_SETTINGS.get(name, default))

    __getitem__ = get


class Manager(AbstractManager):
    def create_url(self, endpoint, *endpoint_args, **endpoint_kwargs):
        return reverse_lazy(endpoint, args=endpoint_args, kwargs=endpoint_kwargs)

    def get_flash_messages(self):
        if self.context is None:
            raise Error('Context required.')

        for message in self.context['messages']:
            yield FlashedMessage(
                message.level_tag, message.message, message.level_tag, message_class=message.extra_tags
            )


config = ConfigWrapper()
manager = Manager()
manager.home_page = config['ADMINLTE_HOME_PAGE']
