from adminlte_full.menu import MenuItem, Menu

from django.shortcuts import render
from django.contrib import messages


def dashboard(request):
    messages.debug(request, '%s SQL statements were executed.' % 666)
    messages.info(request, 'Three credits remain in your account.')
    messages.success(request, 'Profile details updated.')
    messages.warning(request, 'Your account expires in three days.')
    messages.error(request, 'Document deleted.')
    return render(request, 'dashboard.html')


def menu_builder(sender, **kwargs):
    single_menuitem_1 = MenuItem(1, 'Dashboard', 'home')
    sender.add_item(single_menuitem_1)


Menu.show_signal.connect(menu_builder)
