import django.dispatch
from django.urls import reverse, resolve
from collections import OrderedDict


class MenuItem(object):
    COLOR_AQUA = 'aqua'
    COLOR_GREEN = 'green'
    COLOR_RED = 'red'
    COLOR_YELLOW = 'yellow'

    def __init__(self, uid, label, route, route_args=None, icon=False, badge=False, badge_color=None):
        self.__active = False
        self.__parent = None
        self.__children = []
        self.__route_args = route_args or {}

        self.uid = uid
        self.label = label
        self.route = route
        self.icon = icon
        self.badge = badge
        self.badge_color = badge_color or self.COLOR_GREEN

    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, active):
        self.__active = bool(active)

        if self.has_parent():
            self.parent.active = self.parent.has_active_child()

    def add_child(self, child):
        if isinstance(child, MenuItem):
            child.parent = self
            self.__children.append(child)

    @property
    def children(self):
        return self.__children

    @children.setter
    def children(self, children):
        for child in children:
            self.add_child(child)

    def has_active_child(self):
        for child in self.children:
            if child.is_active():
                return True
        return None

    def has_children(self):
        return bool(self.children)

    def has_parent(self):
        return isinstance(self.parent, MenuItem)

    def is_active(self):
        return bool(self.active)

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, parent):
        if isinstance(parent, MenuItem):
            self.__parent = parent

    def remove_child(self, child):
        if child in self.children:
            self.children.remove(child)

    @property
    def route_args(self):
        return self.__route_args

    @route_args.setter
    def route_args(self, route_args):
        if isinstance(route_args, dict):
            self.__route_args = route_args

    def url(self):
        if self.route is not None:
            return reverse(self.route, kwargs=self.route_args)
        return ''


class Menu(object):
    show_signal = django.dispatch.Signal()

    def __init__(self):
        self.__items = OrderedDict()

    def __activate_by_path(self, path, items):
        for item in items:
            if item.has_children():
                self.__activate_by_path(path, item.children)
            else:
                item.active = self.__path_equals_route(path, item.route)

    def __path_equals_route(self, path, route):
        resolved = False

        try:
            resolved = resolve(path)
        except:
            pass

        return resolved and resolved.url_name == route

    def activate_by_context(self, context):
        self.__activate_by_path(
            context.get('request').path, self.items.values()
        )

    def add_item(self, item):
        if isinstance(item, MenuItem):
            self.__items[item.uid] = item

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, items):
        for item in items:
            self.add_item(item)

    def root_item(self, uid):
        return self.items.get(uid)
