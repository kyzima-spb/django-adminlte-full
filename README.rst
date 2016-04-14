=====
django-adminlte-full
=====

This Django application is port the [AdminLTE Template](https://github.com/almasaeed2010/AdminLTE) for easy integration into Django Framework

Quick start
-----------

1. Add "adminlte_full" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'adminlte_full',
    ]

2. Include the panels URLconf in your project urls.py like this::

    url(r'^<url_url>/', include('adminlte_full.urls')),
