"""
Add icons to the links using the .nav-icon class with font-awesome or any other icon font library
"""
from adminlte_base import MenuItemMixin, MenuMixin, MenuItem
from django.db import models


class MenuItemModel(models.Model, MenuItemMixin):
    TYPES = (
        (MenuItem.TYPE_LINK, MenuItem.TYPE_LINK.title()),
        (MenuItem.TYPE_HEADER, MenuItem.TYPE_HEADER.title()),
        (MenuItem.TYPE_DROPDOWN_DIVIDER, MenuItem.TYPE_DROPDOWN_DIVIDER.title()),
    )
    menu = models.ForeignKey('MenuModel', on_delete=models.PROTECT)
    parent = models.ForeignKey(
        'self', on_delete=models.PROTECT, null=True, blank=True
    )
    type = models.CharField(
        max_length=20, default=MenuItem.TYPE_LINK, choices=TYPES
    )
    title = models.CharField(max_length=500)
    url = models.URLField(max_length=500, blank=True)
    endpoint = models.CharField(max_length=255, blank=True)
    endpoint_args = models.TextField(blank=True)
    endpoint_kwargs = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)
    help = models.CharField(max_length=500, blank=True)
    pos = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f'{self.menu.title} - {self.title}'


class MenuModel(models.Model, MenuMixin):
    title = models.CharField(max_length=500)
    program_name = models.CharField(max_length=255, unique=True)

    @property
    def items(self):
        return self.menuitemmodel_set.select_related('parent')

    def __str__(self):
        return f'{self.title} [{self.program_name}]'
