from adminlte_base import Collection
import django.dispatch


class Dropdown(Collection):
    def __init__(self, context):
        super().__init__()
        self.context = context


class MessageDropdown(Dropdown):
    """Messages sent to the user."""
    show_signal = django.dispatch.Signal()


class NotificationDropdown(Dropdown):
    """Notifications sent to the user."""
    show_signal = django.dispatch.Signal()


class TaskDropdown(Dropdown):
    """Task in progress."""
    show_signal = django.dispatch.Signal()
