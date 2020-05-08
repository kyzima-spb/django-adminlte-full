from django.dispatch import Signal


menu_loaded = Signal(providing_args=['menu', 'program_name', 'context'])
messages_loaded = Signal(providing_args=['messages', 'context'])
notifications_loaded = Signal(providing_args=['notifications', 'context'])
tasks_loaded = Signal(providing_args=['tasks', 'context'])
