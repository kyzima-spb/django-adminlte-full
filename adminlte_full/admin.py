from django.contrib import admin

from . import models

admin.site.register(models.MenuModel)
admin.site.register(models.MenuItemModel)
