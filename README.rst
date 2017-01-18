=====
django-adminlte-full
=====

This Django application is port the `AdminLTE Template <https://github.com/almasaeed2010/AdminLTE>`_ for easy integration into Django Framework

Quick start
-----------

1. Add "bootstrap3" and "adminlte_full" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'bootstrap3',
        'adminlte_full',
    ]

2. Include the panels URLconf in your project urls.py like this::

    url(r'^<url_url>/', include('adminlte_full.urls')),

Building an HTML menu
---------------------

This application offers these elements to ease the construction of the HTML markup expected by AdminLTE to render the sidebar menu:

* A `template tag <adminlte_full/templatetags/adminlte_full.py>`_ named *show_menu*, which is already used by the `base-layout.html template file <adminlte_full/templates/adminlte_full/base-layout.html>`_ so you have to do nothing to render the menu!
* A `couple of classes <adminlte_full/menu.py>`_: MenuItem and Menu, which handle the inner data structure of the menu hierarchy and are agnostic and neutral about how you decide which items, links and parent-child relationships will be in the final menu
* A `Django Signal <https://docs.djangoproject.com/en/1.9/topics/signals/>`_ available for you to get a chance to add MenuItem instances to the Menu object created by the *show_menu* tag

A simple real example would be involve some files, like the following ones.

* The URLs patterns file::

    # urls.py
    from django.conf.urls import url
    from my_app.views import my_view_1, my_view_2, my_view_3
    urlpatterns = [
        url(r'^$', my_view_1, name='index'),
        url(r'^$', my_view_2, name='view_2'),
        url(r'^$', my_view_3, name='view_3'),
    ]

* The views file::

    # views.py
    from adminlte_full.menu import MenuItem, Menu
    from django.shortcuts import render

    def my_view_1(request):
        return render(request, 'my_app/template_1.html')

        def my_view_2(request):
        return render(request, 'my_app/template_2.html')

    def my_view_3(request):
        return render(request, 'my_app/template_3.html')

    def my_menuitems_builder(sender, **kwargs):
        # sender is an instance of Menu class
        single_menuitem_1 = MenuItem(1, 'Index', 'index')
        parent_menuitem_2 = MenuItem(2, 'Parent Menu', '#')
        single_menuitem_3 = MenuItem(3, 'Index', 'view_2')
        single_menuitem_4 = MenuItem(4, 'Index', 'view_3')
        
        user=kwargs['context']['user']
        if user.has_perm('app.view_data'):
            single_menuitem_5 = MenuItem(5, 'Data', 'dataview')
            sender.add_item(sender.add_child(single_menuitem_5))
        
        parent_menuitem_2.add_child(single_menuitem_3)
        parent_menuitem_2.add_child(single_menuitem_4)
        sender.add_item(single_menuitem_1)
        sender.add_item(parent_menuitem_2)
        
    Menu.show_signal.connect(my_menuitems_builder)

* The template file::

    {# templates/my_app/template_1.html #}
    {% extends "adminlte_full/base-layout.html" %}

    {% block page_title %}Title One{% endblock %}

    {% block page_content %}
        <h1>My header one</h1>
        <p>My content one</p>
    {% endblock %}
