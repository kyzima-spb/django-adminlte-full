Django-AdminLTE-Full
====================

This Django application is port the `AdminLTE`_ for easy integration into `Django`_ Framework.

Installation
------------

1. Install the latest stable version::

    $ pip install django-adminlte-full

   or install development version (bugs are possible)::

    $ pip install https://github.com/kyzima-spb/django-adminlte-full/archive/dev-master.zip

2. In the settings, add ``crispy_forms`` and ``adminlte_full`` to your ``INSTALLED_APPS``, like this::

    INSTALLED_APPS = [
        ...
        'crispy_forms',
        'adminlte_full',
    ]

3. In the settings, set the value of the ``CRISPY_TEMPLATE_PACK`` option as ``'bootstrap4'``::

    CRISPY_TEMPLATE_PACK = 'bootstrap4'

4. In the settings, add ``adminlte`` to the list of context processors, like this::

    TEMPLATES = [
        {
            ...
            'OPTIONS': {
                'context_processors': [
                    ...
                    'adminlte_full.context_processors.adminlte',
                ],
            },
        },
    ]

5. Include the URLconf in your project ``urls.py`` like this::

    path('', include('adminlte_full.urls'))

Documentation
-------------
`Continue reading the documentation.`_


.. _Django: https://www.djangoproject.com/
.. _AdminLTE: https://adminlte.io/
.. _Continue reading the documentation.: https://adminlte-full.readthedocs.io/en/latest/django.html
