`django-longer-user-fields` provides a migration and a monkeypatch to make the django auth.user fields longer, instead of the arbitrarily short 30 characters.

It allows you to update the length of the ``username``, ``first_name`` and ``last_name`` fields.

It's designed to be a simple include-and-forget project that makes a little headache go away.  Enjoy, and pull requests welcome!

Usage
=====
Step 1. Install django-longer-user-fields. 
-------------------------------------

- `pip install django-longer-user-fields` 

You will also need to install [south]() to use the migration. 

 - `pip install south` 


Step 2. Add `longeruserfields` to your installed apps.
-------------------------
Add 'longeruserfields' to the top of your `INSTALLED_APPS` in settings.py

settings.py

```python
INSTALLED_APPS = ("longeruserfields",) + INSTALLED_APPS
```

Step 3. (Optional) Specify custom fields lengths
-------------------------------------------------
If you want to specify a custom length, add it to settings.py. The default is 255 characters.

settings.py

```python
MAX_USERNAME_LENGTH = 100  # optional, default is 255.
MAX_FIRSTNAME_LENGTH = 80  # optional, default is 255.
MAX_LASTNAME_LENGTH = 80   # optional, default is 255.
```



Step 4. Run the migration
------------------------------------------------
```
$ python manage.py migrate longeruserfields
```

That's it, you should be good to go!


Notes about the built-in forms
==============================
This app also automatically monkey patches the User forms in the Django admin to remove the 30 character limit.

It provides a suitable replacement for the standard AuthenticationForm as well, but due to the implementation you must manually utilize it.

urls.py

```python
from longeruserfields.forms import AuthenticationForm

urlpatterns = patterns('',
    # ...
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'authentication_form': AuthenticationForm}),
)
```

Credits
=======

The monkeypatch for this is very largely based on [celement's answer on stackoverflow](http://stackoverflow.com/questions/2610088/can-djangos-auth-user-username-be-varchar75-how-could-that-be-done)

This ``django-longer-user-fields`` project is a fork of the [``django-longer-username`` project](https://github.com/GoodCloud/django-longer-username).
