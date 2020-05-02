from adminlte_base import menu
import django.dispatch
from django.urls import reverse_lazy


class MenuItem(menu.MenuItem):
    def __init__(self, id_item, title, parent=None,
                 url=None, endpoint=None, endpoint_args=None, endpoint_kwargs=None,
                 item_type=None, icon=False, help=None, badge=None):

        if not (bool(url) ^ bool(endpoint)):
            raise TypeError('You need to set the value of only one of the arguments: url or endpoint.')

        if endpoint is not None:
            url = reverse_lazy(endpoint, args=endpoint_args, kwargs=endpoint_kwargs)

        super().__init__(id_item, title, url, parent=parent,
                         item_type=item_type, icon=icon, help=help, badge=badge)


class Menu(menu.Menu):
    show_signal = django.dispatch.Signal()

    def activate_by_path(self, path):
        """Makes active a menu item whose URL matches the one specified in the argument."""
        for item in self._items.values():
            if item.url == path:
                item.set_active(True)
                return True
        return False

    def activate_by_context(self, context):
        """Makes active the menu item whose URL matches the current from the request."""
        return self.activate_by_path(context['request'].path)
