0.2.0
=====

- Upgrading to Bootstrap 4 and AdminLTE 3.
- Signals are renamed, moved to the `signals.py` module and no longer have a class binding:

  - `menu_loaded(menu, program_name, context)` - triggered when the application menu was created.
  - `messages_loaded(messages, context)` - triggered when the drop-down list with incoming messages was created.
  - `notifications_loaded(notifications, context)` - triggered when a dropdown list with notifications was created.
  - `tasks_loaded(tasks, context)` - triggered when a drop-down list with tasks being performed was created.

  Signals are left as a simpler extension option, their use is not necessary, moreover, the signals will not work without loaders.

- The manager provides the following decorators for loaders:

  - `@manager.menu_loader` - sets the callback for loading a menu from the database or other source. It has a default implementation.
  - `@manager.messages_loader` - sets the callback for loading a messages from the database or other source.
  - `@manager.notifications_loader` - sets the callback for loading a notifications from the database or other source.
  - `@manager.tasks_loader` - sets the callback for loading a tasks from the database or other source.

- The extension depends on the `adminlte-base` package, into which all the basic logic has been moved.
- The application menu is now stored in the database.
- The following context managers have been added:

  - `config` - getting the configuration parameter in the template.

- The following template filters are added:

  - `gravatar` - getting an avatar using the Gravatar service.
  - `humanize` - date output in human-readable format.

- Full integration with Django authentication system.

0.1.1
=====

The release was added only to maintain backward compatibility. All new code will no longer work with the old version.