"""
Add icons to the links using the .nav-icon class with font-awesome or any other icon font library
"""
from adminlte_base.menu import MenuItem
from django.db import models


class MenuItemModel(models.Model):
    TYPES = (
        (MenuItem.TYPE_LINK, MenuItem.TYPE_LINK.title()),
        (MenuItem.TYPE_HEADER, MenuItem.TYPE_HEADER.title()),
    )
    menu = models.ForeignKey('MenuModel', on_delete=models.PROTECT)
    parent = models.ForeignKey(
        'self', on_delete=models.PROTECT, null=True, blank=True
    )
    type = models.CharField(
        max_length=20, default=MenuItem.TYPE_LINK, choices=TYPES
    )
    # url = models.URLField()
    endpoint = models.CharField(max_length=255)
    endpoint_args = models.TextField(blank=True)
    endpoint_kwargs = models.TextField(blank=True)
    title = models.CharField(max_length=500)
    icon = models.CharField(
        max_length=50, default='far fa-circle', blank=True
    )
    help = models.CharField(max_length=500, blank=True)
    pos = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return f'{self.menu.title} - {self.title}'

    def get_endpoint_args(self):
        return self.endpoint_args.split()

    def get_endpoint_kwargs(self):
        return dict(p.split('=') for p in self.endpoint_kwargs.splitlines())


class MenuModel(models.Model):
    title = models.CharField(max_length=500)
    program_name = models.CharField(max_length=255, unique=True)

    @property
    def items(self):
        return self.menuitemmodel_set.select_related('parent').order_by('parent', 'pos').all()

    def __str__(self):
        return f'{self.title} [{self.program_name}]'
