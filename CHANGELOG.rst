CHANGELOG
=========

0.2.0
-----

- Upgrading to Bootstrap 4 and AdminLTE 3.
- Full integration with Django authentication system.
- Added pages for 400, 403, 404 and 500 errors.
- The ``django-bootstrap`` dependency has been replaced with a more functional ``django-crispy-form``.
- Color skins for sidebar, navbar and logo.
- The manager provides the following decorators for loaders:

  - ``manager.@home_page_getter`` - sets a callback to get the home page.
  - ``@manager.menu_loader`` - sets the callback for loading a menu from the database or other source.
  - ``@manager.messages_loader`` - sets the callback for loading a messages from the database or other source.
  - ``@manager.notifications_loader`` - sets the callback for loading a notifications from the database or other source.
  - ``@manager.tasks_loader`` - sets the callback for loading a tasks from the database or other source.
  - ``@manager.user_getter`` - sets a callback to get the original user object. It has a default implementation.

- The extension depends on the ``adminlte-base`` package, into which all the basic logic has been moved.
- The application menu is now stored in the database.
- The following context managers have been added:

  - ``config`` - getting the configuration parameter in the template.
  - ``ThemeColor`` - color styles.
  - ``ThemeLayout`` - layout Options.
  - ``adminlte_user`` - current user.

- The following template filters are added:

  - ``gravatar`` - getting an avatar using the Gravatar service.
  - ``humanize`` - date output in human-readable format.

- Almost all classes, functions and templates from the previous release are removed. All signals are also deleted.

0.1.1
-----

The release was added only to maintain backward compatibility. All new code will no longer work with the old version.